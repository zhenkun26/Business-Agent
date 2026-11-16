"""Provider-aligned analysis with exact money and deterministic reports."""
from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
import html
import re
import time
from typing import Any

from app.agents.knowledge import AgentResult
from app.tools.analysis_data import AnalysisDataError, AnalysisReader, authorize, iso_date


# This is a bounded query language, not a general natural-language interpreter.
DATE_TOKEN = r'(?<![0-9])\d{4}-\d{2}-\d{2}(?![0-9])'
RELATIVE_PERIOD = (r'本月|上月|今年|去年|季度|最近|昨天|今天|同比|环比|'
                   r'(?<![A-Za-z0-9_-])\d{4}(?![A-Za-z0-9_-])|\d+年|\d+月|\d+天|'
                   r'\b(?:last|this|next|quarter|year|month|today|yesterday|recent)\b')
STATUS_TERMS = {'pending': r'待处理|待完成|\bpending\b',
                'completed': r'已完成|\bcompleted\b',
                'cancelled': r'已取消|\bcancelled\b',
                'refunded': r'已退款|\brefunded\b'}


def parse_range(query: str) -> tuple[str | None, str | None]:
    dates = re.findall(DATE_TOKEN, query)
    if dates and (len(dates) != 2 or iso_date(dates[0]) > iso_date(dates[1])):
        raise AnalysisDataError('ANALYSIS_RANGE_INVALID')
    if re.search(RELATIVE_PERIOD, re.sub(DATE_TOKEN, ' ', query), re.I):
        raise AnalysisDataError('ANALYSIS_RANGE_UNSUPPORTED')
    if not dates and re.search(r'\b(?:from|to|between)\b|从|至|到', query, re.I):
        raise AnalysisDataError('ANALYSIS_RANGE_UNSUPPORTED')
    return (dates[0], dates[1]) if dates else (None, None)


def query_selection(query: str, known: set[str]) -> tuple[set[str], list[str]]:
    """Consume every meaningful token; unknown scope cannot silently become all rows."""
    parse_range(query)
    remaining = re.sub(DATE_TOKEN, ' ', query)
    if re.search(r'\b(?:by|per)\b(?!\s+(?:the\s+)?customers?\b)|按(?!各?客户)', remaining, re.I):
        raise AnalysisDataError('ANALYSIS_METRIC_UNSUPPORTED')
    # Preserve the existing explicit unsupported-metric error contract.
    if re.search(r'营收|收入|销售额|净额|排名|前[一二三四五六七八九十\d]+|'
                 r'行业|趋势|占比|比例|差值|增长|平均|最大|最小|中位|分布|'
                 r'\b(?:revenue|rank\w*|top|average|mean|median|max\w*|min\w*|'
                 r'not|except|excluding|without)\b|不含|排除|除外|未完成|非|不', remaining, re.I):
        raise AnalysisDataError('ANALYSIS_METRIC_UNSUPPORTED')
    requested: set[str] = set()
    folded: dict[str, list[str]] = defaultdict(list)
    for cid in known:
        folded[cid.casefold()].append(cid)

    def select(match: re.Match[str]) -> str:
        value = match.group(1) if match.lastindex else match.group()
        candidates = folded.get(value.casefold(), [])
        if len(candidates) != 1:
            raise AnalysisDataError('ANALYSIS_ENTITY_UNAVAILABLE')
        requested.add(candidates[0])
        return ' '

    remaining = re.sub(r'(?:\bcustomer\b|客户)\s*[:=]\s*([A-Za-z0-9_-]+)',
                       select, remaining, flags=re.I)
    remaining = re.sub(r'(?:\bcustomer\b|客户)\s+(C\d[A-Za-z0-9_-]*)',
                       select, remaining, flags=re.I)
    remaining = re.sub(r'(?<![A-Za-z0-9_-])C\d[A-Za-z0-9_-]*',
                       select, remaining, flags=re.I)
    # Opaque IDs require an explicit customer: selector to avoid consuming metric words.
    if re.search(r'\bfor\s+(?:the\s+)?customer\b|(?:\bcustomer\b|客户)\s*[:=]', remaining, re.I):
        raise AnalysisDataError('ANALYSIS_ENTITY_UNAVAILABLE')
    statuses = []
    for status, pattern in STATUS_TERMS.items():
        if re.search(pattern, remaining, re.I):
            statuses.append(status)
            remaining = re.sub(pattern, ' ', remaining, flags=re.I)
    if ((requested and statuses and re.search(r'\bor\b|或', remaining, re.I))
            or (len(statuses) > 1 and re.search(r'\bcompare\b|对比|比较', remaining, re.I))):
        raise AnalysisDataError('ANALYSIS_METRIC_UNSUPPORTED')
    # Only neutral report words/connectors may remain. No arbitrary suffix is ignored.
    remaining = re.sub(r'\b(?:show|list|summarize|sum|total|count|compare|analyze|analysis|'
                       r'order|orders|amount|amounts|value|values|customer|customers|'
                       r'by|per|for|of|the|their|all|available|and|or|from|to|between|please)\b',
                       ' ', remaining, flags=re.I)
    remaining = re.sub(r'请|一下|统计|汇总|分析|对比|比较|展示|显示|查询|订单|原始金额|总额|金额|数量|'
                       r'客户|各|所有|全部|可用|按|的|和|与|或|从|至|到|期间', ' ', remaining)
    if re.sub(r'[\s,，。.!！?？、:：=;；]+', '', remaining):
        code = ('ANALYSIS_ENTITY_UNAVAILABLE' if re.search(r'客户|\bcustomer\b', query, re.I)
                else 'ANALYSIS_METRIC_UNSUPPORTED')
        raise AnalysisDataError(code)
    if not re.search(r'订单|统计|汇总|分析|对比|比较|\b(?:orders?|sum|total|count|compare|analy[sz]e)\b', query, re.I):
        raise AnalysisDataError('ANALYSIS_METRIC_UNSUPPORTED')
    return requested, statuses or list(STATUS_TERMS)


def compute(query: str, snapshot: dict[str, Any]) -> dict[str, Any]:
    orders = snapshot['orders']
    requested, statuses = query_selection(query, {o['customer_id'] for o in orders})
    selected = [o for o in orders if (not requested or o['customer_id'] in requested)
                and o['status'] in statuses]
    customers = {c['customer_id']: c for c in snapshot['customers']}
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for order in selected:
        groups[(order['customer_id'], order['currency'])].append(order)
    rows = []
    totals: dict[str, dict[str, int]] = {}
    for (cid, currency), values in sorted(groups.items()):
        amount = sum(o['amount_minor'] for o in values)
        rows.append({'customer_id': cid, 'currency': currency,
            'name': customers.get(cid, {}).get('name'), 'order_amount_minor': amount,
            'order_count': len(values)})
        total = totals.setdefault(currency, {'order_amount_minor': 0, 'order_count': 0})
        total['order_amount_minor'] += amount
        total['order_count'] += len(values)
    dates = [o['created_at'] for o in selected]
    return {'rows': rows, 'totals_by_currency': totals,
        'selected_customer_ids': sorted(requested) if requested else None,
        'observed_range': {'start_date': min(dates) if dates else None,
                           'end_date': max(dates) if dates else None},
        'provenance': snapshot['provenance'],
        'statuses_included': statuses,
        'revenue': None}


def cell(value: Any) -> str:
    return html.escape(str(value or '-')).replace('|', '&#124;').replace(
        '\n', ' ').replace('\\', '&#92;').replace('`', '&#96;')


def money(value: int) -> str:
    return format(Decimal(value) / 100, ',.2f')


def render(data: dict[str, Any]) -> str:
    provenance = data['provenance']
    period = provenance['requested_range']
    start, end = period['start_date'], period['end_date']
    scope = f'{start} 至 {end}（含首尾，UTC 日期）' if start else '全部可用订单日期'
    observed = data['observed_range']
    lines = [
        '数据来源：' + ('Mock 内置样例（非真实业务）' if provenance['is_mock']
                        else 'HTTP 参考 CRM（非企业现场验收）'),
        f"快照：{cell(provenance['snapshot_id'])}；截至 {cell(provenance['as_of'])}。",
        f"读取时间：{cell(provenance['fetched_at'])}；请求范围：{scope}。",
        f"实际订单日期：{cell(observed['start_date'])} 至 {cell(observed['end_date'])}。",
        '口径：订单原始金额；纳入状态 ' + ', '.join(data['statuses_included']) +
        '。不代表净收入或累计销售额。',
        '金额按币种分别汇总；参考契约统一使用两位小数。',
    ]
    if not data['rows']:
        return '\n\n'.join(lines + ['该范围内没有可分析的订单。'])
    lines += ['', '| 客户 ID | 客户名称 | 币种 | 订单金额 | 订单数 |',
              '| --- | --- | --- | ---: | ---: |']
    for row in data['rows']:
        lines.append(f"| {cell(row['customer_id'])} | {cell(row['name'])} | "
                     f"{row['currency']} | {money(row['order_amount_minor'])} | "
                     f"{row['order_count']} |")
    for currency, total in sorted(data['totals_by_currency'].items()):
        lines.append(f"合计 {currency}：{money(total['order_amount_minor'])}，"
                     f"订单数 {total['order_count']}。")
    if not provenance['customer_details']:
        lines.append('当前权限不包含客户档案；仅按已授权订单中的客户 ID 分组。')
    return '\n'.join(lines)


class AnalysisAgent:
    def __init__(self, user_role: Any, user_dept: str | None = None,
                 user_id: str | None = None) -> None:
        self.user_role = user_role
        self.user_dept = user_dept
        self.user_id = user_id

    async def run(self, query: str) -> AgentResult:
        start_time = time.monotonic()
        try:
            start, end = parse_range(query)
            reader = AnalysisReader(self.user_id, self.user_role, self.user_dept)
            snapshot = await reader.read(start, end)
            data = compute(query, snapshot)
            await authorize(self.user_id, self.user_role, self.user_dept)
            has_data = bool(data['rows'])
            return AgentResult(
                agent_name='analysis', success=True, confidence=.8 if has_data else 0,
                output={'answer': render(data), 'data': data, 'deterministic': True,
                        'coverage': 'full' if has_data else 'none',
                        'stage': 'analysis_complete' if has_data else 'analysis_empty'},
                sources=[], needs_replan=False,
                latency_ms=int((time.monotonic() - start_time) * 1000))
        except Exception as exc:
            code = str(exc) if isinstance(exc, AnalysisDataError) else 'ANALYSIS_SOURCE_UNAVAILABLE'
            return AgentResult(agent_name='analysis', success=False, confidence=0,
                output={'answer': '分析未完成：' + code + '。请检查权限与数据源。支持订单原始金额与数量汇总，例如“统计客户 C001 的已完成订单”；日期需明确起止日期。排名、平均值、排除条件及姓名查询暂不支持。',
                        'deterministic': True, 'coverage': 'none', 'stage': 'analysis_blocked'},
                error=code, sources=[], needs_replan=False,
                latency_ms=int((time.monotonic() - start_time) * 1000))
