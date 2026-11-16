"""Execute actual list SQL in memory; PostgreSQL JSON membership alone is adapted.

This verifies relational paging, not PostgreSQL driver or live transaction acceptance.
"""
import ast
from datetime import datetime
import json
from pathlib import Path
import sqlite3
from types import SimpleNamespace as NS
from unittest import IsolatedAsyncioTestCase

from fastapi import HTTPException


class ApprovalPaginationTests(IsolatedAsyncioTestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.addCleanup(self.connection.close)
        self.connection.row_factory = sqlite3.Row
        self.connection.create_function('has_role', 2, lambda roles, role: role in json.loads(roles))
        self.connection.execute('CREATE TABLE approval_requests ('
            'approval_id TEXT PRIMARY KEY, session_id TEXT, operation_type TEXT, risk_level TEXT, '
            'summary TEXT, created_at TEXT, batch_id TEXT, status TEXT, requester_id TEXT, '
            'prefill_payload TEXT, approver_roles TEXT, expires_at TEXT, approval_contract TEXT, '
            'approver_id TEXT, comment TEXT, decided_at TEXT)')
        for i in range(105):
            own = i < 53
            self.connection.execute('INSERT INTO approval_requests VALUES '
                '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (f'a{i:03}', 's', 'action', 'high', 'Synthetic', '2026-11-15T00:00:00',
                 None, 'pending', 'u' if own else 'other', '{}',
                 '["manager"]' if own else '["admin"]', None, '{}',
                 'u' if own else 'other', None, '2026-11-15T01:00:00'))
        self.calls = []
        source = Path(__file__).resolve().parents[1] / 'app/api/approval.py'
        tree = ast.parse(source.read_text())
        names = {'_approval_page', 'list_pending_approvals', 'list_my_approvals',
                 'list_handled_approvals'}
        tree.body = [node for node in tree.body if getattr(node, 'name', None) in names]
        for node in tree.body:
            node.decorator_list = []
        self.scope = dict(Any=object, User=NS, HTTPException=HTTPException,
                          Depends=lambda value: None, get_current_user=None, get_db=None,
                          text=lambda value: value,
                          deadline=NS(review_fields=lambda row: {'human_review_required': True}))
        exec(compile(tree, str(source), 'exec'), self.scope)
        self.actor = NS(user_id='u', role='manager')

    async def execute(self, sql, params):
        self.calls.append((sql, params))
        sql = sql.replace('approver_roles ? :actor', 'has_role(approver_roles, :actor)')
        records = []
        for raw in self.connection.execute(sql, params).fetchall():
            row = dict(raw)
            for key in ('created_at', 'decided_at'):
                if row[key] is not None:
                    row[key] = datetime.fromisoformat(row[key])
            records.append(NS(**row))
        return NS(fetchall=lambda: records)

    async def page(self, kind, **kwargs):
        name, parameter = {
            'pending': ('list_pending_approvals', 'approver'),
            'mine': ('list_my_approvals', 'requester'),
            'handled': ('list_handled_approvals', 'requester'),
        }[kind]
        return await self.scope[name](**{parameter: self.actor, 'db': self, **kwargs})

    async def test_all_three_lists_reach_every_row_once_with_timestamp_ties(self):
        for kind in ('pending', 'mine', 'handled'):
            with self.subTest(kind=kind):
                first = await self.page(kind)
                second = await self.page(kind, offset=50)
                self.assertEqual(first['total'], 53)
                self.assertEqual(first['returned_count'], 50)
                self.assertTrue(first['has_more'])
                self.assertEqual(second['total'], 53)
                self.assertEqual(second['returned_count'], 3)
                self.assertFalse(second['has_more'])
                ids = [row['approval_id'] for row in first['items'] + second['items']]
                self.assertEqual(ids, [f'a{i:03}' for i in reversed(range(53))])
                self.assertTrue(all(row['human_review_required'] for row in first['items']))
        self.assertEqual(len(self.calls), 6)  # Count and page share one statement.

    async def test_empty_and_out_of_range_pages_keep_the_real_total(self):
        for kind in ('pending', 'mine', 'handled'):
            result = await self.page(kind, offset=500)
            self.assertEqual(result['total'], 53)
            self.assertEqual(result['items'], [])
            self.assertFalse(result['has_more'])
        self.actor = NS(user_id='missing', role='salesperson')
        for kind in ('pending', 'mine', 'handled'):
            result = await self.page(kind)
            self.assertEqual(result['total'], 0)
            self.assertEqual(result['items'], [])

    async def test_pending_count_is_global_and_excludes_nonpending(self):
        self.connection.execute("UPDATE approval_requests SET status='approved' WHERE approval_id='a000'")
        result = await self.page('pending', limit=1)
        self.assertEqual(result['pending_count'], 52)
        self.assertEqual(result['returned_count'], 1)

    async def test_actor_scope_is_reapplied_on_every_page(self):
        self.actor = NS(user_id='other', role='admin')
        for kind in ('pending', 'mine', 'handled'):
            result = await self.page(kind, offset=50)
            self.assertEqual(result['total'], 52)
            self.assertEqual([row['approval_id'] for row in result['items']], ['a054', 'a053'])

    async def test_actor_values_are_bound_not_interpolated(self):
        self.actor = NS(user_id="u' OR 1=1 --", role="manager' OR 1=1 --")
        for kind in ('pending', 'mine', 'handled'):
            result = await self.page(kind)
            self.assertEqual(result['total'], 0)
            self.assertNotIn('OR 1=1', self.calls[-1][0])

    async def test_invalid_page_bounds_fail_before_sql(self):
        for kind in ('pending', 'mine', 'handled'):
            for values in ({'limit': 0}, {'limit': 101}, {'limit': True}, {'offset': -1},
                           {'offset': 1_000_001}, {'offset': 1.5}):
                with self.subTest(kind=kind, values=values):
                    with self.assertRaises(HTTPException) as caught:
                        await self.page(kind, **values)
                    self.assertEqual(caught.exception.status_code, 422)
        self.assertFalse(self.calls)

    async def test_null_handled_timestamps_sort_last(self):
        self.connection.execute("UPDATE approval_requests SET decided_at=NULL WHERE approval_id='a052'")
        result = await self.page('handled', offset=50)
        self.assertEqual([row['approval_id'] for row in result['items']], ['a001', 'a000', 'a052'])

    async def test_exact_boundary_and_maximum_limit(self):
        self.connection.execute("UPDATE approval_requests SET requester_id='other' WHERE approval_id IN ('a000','a001','a002')")
        result = await self.page('mine')
        self.assertEqual(result['total'], 50)
        self.assertFalse(result['has_more'])
        result = await self.page('pending', limit=100)
        self.assertEqual(result['returned_count'], 53)
        self.assertFalse(result['has_more'])
