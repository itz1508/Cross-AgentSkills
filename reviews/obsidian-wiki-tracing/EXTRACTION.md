# Source extraction — Obsidian Wiki tracing candidates

**Summary:** The original `wiki-rebuild` skill is preserved verbatim; the other tracing candidates are summarized from the upstream instructions for future review, not installed or executed.

## Provenance

- Repository: https://github.com/Ar9av/obsidian-wiki
- Inspected branch: `main`; reference commit: `acc0ac1769349c7550696724f564b0ca719e146c`
- Extracted original: `skills/wiki-rebuild/SKILL.md`, Git blob `a83e15574aa176256464fd0f85ce0c421d108577`.
- License: MIT; the copied `LICENSE` is the original license text.
- Local source copy: [`wiki-rebuild-SKILL.md`](wiki-rebuild-SKILL.md), preserved byte-for-byte (Git blob verified).
- Extraction is a *reference snapshot*, not a locally installed skill and not a command to rebuild anything.

## Functionality extracted from source

| Upstream skill | Source path | Actual purpose | OneShot relevance |
|---|---|---|---|
| `wiki-rebuild` | `skills/wiki-rebuild/SKILL.md` | Archive the current Obsidian wiki; clear and re-ingest source knowledge; or restore an archive. Destructive modes need confirmation and an archive. | Disaster recovery for a separately configured wiki, not source-code cleanup or execution tracing. |
| `session-search` | `skills/session-search/SKILL.md` | Query a prebuilt session-brain graph, rank historical sessions, load bounded transcript excerpts, and cite session IDs. It distinguishes loadable transcripts from history-only matches. | Candidate for finding the original session behind a decision, if source history exists and is accessible. |
| `memory-bridge` | `skills/memory-bridge/SKILL.md` | Browse, search, compare, or map compiled wiki pages by originating assistant/source tool using `.manifest.json`. | Candidate for identifying which tool produced a note and cross-tool knowledge gaps. Does not automatically copy model memory. |
| `cross-linker` | `skills/cross-linker/SKILL.md` | Suggest/add Obsidian wikilinks and typed semantic relationships; distinguishes high, medium, and ambiguous linkage. Writes to the vault when invoked. | Candidate for linking related knowledge records; inferred connections are **not** primary-source proof of code execution. |

Verified upstream Git blobs:

- `session-search`: `6621cbed9f29b5c4a2a55bfad84a92688ecf7d0f`
- `memory-bridge`: `f1fb5f829a50974890030b2cddd643a1e81da2b2`
- `cross-linker`: `a5ed6a7448e40f852ea1132ac4945d0fb3f57c5d`

Read the original, pinned sources in GitHub:

- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/session-search/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/memory-bridge/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/cross-linker/SKILL.md
- https://github.com/Ar9av/obsidian-wiki/blob/acc0ac1769349c7550696724f564b0ca719e146c/skills/llm-wiki/SKILL.md

## Original prerequisites and safeguards

- `wiki-rebuild` depends on the configuration resolution protocol defined in `llm-wiki/SKILL.md`, `OBSIDIAN_VAULT_PATH`, and the wiki `.manifest.json`.
- `session-search` assumes an existing session-brain graph; a result may not have a retrievable transcript.
- `memory-bridge` assumes a populated wiki manifest and page-source provenance.
- `cross-linker` may update Markdown content and links; it is **not read-only** when executed.
- `wiki-rebuild` **must not** clear/restore a vault without explicit user confirmation. The source itself says re-ingest must be separately selected.
- QMD is an optional search index, not the authoritative wiki. The original markdown content remains authoritative.

## OneShot interpretation (proposed, not implemented)

1. Keep OneShot Git, contracts, source hashes, task/event stores, and signed/verified Runtime receipts authoritative for execution history.
2. Consider a *read-only projection* from actual records into a searchable knowledge index, rather than letting a wiki define Runtime truth.
3. Link notes by known task/run/source/revision identities when available; never infer them from semantic similarity.
4. Store only distinctive, supported lessons; find before creating and update instead of duplicating.
5. Evaluate the skills with fixture conversations and known-source oracle labels before using them for automatic promotion.

## Status

- Original `wiki-rebuild` file and MIT license **extracted and verified**.
- Other three skills **reviewed and summarized**, with pinned upstream links; their raw files are **not included** in this bundle.
- No installation, wiki mutation, repository change, background monitoring, or integrated execution test performed.
