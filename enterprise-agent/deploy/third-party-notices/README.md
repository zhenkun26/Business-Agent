# Supplemental production notices

These exact upstream texts supplement the licenses retained by installed packages.
The four standalone MIT texts cover langchain-core 1.5.3, langchain-text-splitters
1.1.2, langsmith 0.10.15 and loguru 0.7.3. Their official release-tag sources,
byte hashes and production wheel hashes are recorded in `source-map.json`.

The two `ExtractSchFrom*.xsl.txt` files preserve the complete official Schematron
source, author/history comments and MIT permission notice at commit
77dcd36c53d12ed786c144ece3b2af7694abdc56. They are retained evidence, not executed
or substituted into lxml. Only their transform bodies match the two named lxml
6.1.1 resources: start at the first `<xsl:transform`, normalize CRLF to LF, then
remove trailing LF characters only. The full original files are not byte-identical.
The source map records both original wheel-member hashes and normalized-body hashes.
Preserve lxml's original resources and LICENSES.txt, including its older unlicensed
statement; the later located file-level grant is separate supplemental evidence.

Dockerfile.prod copies this directory to `/app/deploy/third-party-notices`.
The build-input check verifies the source copies. The separate `--installed` check
reads the actual final location, rejects missing, extra, symlinked or changed files,
and exports its scoped byte-verification receipt in installed-inventory.json.
A source check or synthetic test is not evidence that an image already contains them.

These additions do not audit all wheel/native/vendor/OS components, decide license
compatibility or source-offer obligations, or clear project source-rights records.
Preserve existing licenses and notices with each distribution. Distribution, runtime,
full RAG and C10 acceptance remain separately blocked/open.
