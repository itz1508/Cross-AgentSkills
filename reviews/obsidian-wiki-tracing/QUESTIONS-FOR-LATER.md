# Questions for a later OneShot tracing evaluation

**Summary:** Thirty source-testable questions for deciding whether history retrieval and cross-agent knowledge tracing add value without duplicating OneShot execution records.

**Status:** REVIEW QUESTIONS — not an approved plan, completed test, or implementation instruction.  
**Source basis:** Obsidian Wiki's `session-search`, `memory-bridge`, `cross-linker`, and `wiki-rebuild`; adapted to OneShot, not claimed by upstream.  
**Evaluation rule:** For each answer, record the exact source reference, observation, missing evidence, and an independently labeled GOOD/BAD fixture where applicable. Never infer execution authority from a summary.

## A. Existing sources and ownership

Q01. Which actual repository, branch, bootstrap instructions, and stage contracts govern the candidate evaluation?  
Q02. Which source-of-truth records already capture requirements, messages, task/run IDs, revisions, file actions, and verification evidence?  
Q03. Which continuity failures are demonstrated by source evidence rather than reported impressions alone?  
Q04. Can an existing search interface answer each problem without creating a second index, manifest, or graph?  
Q05. Which subsystem owns session retrieval, and which owns live tool/event execution tracing? Where is the boundary enforced?

## B. Session retrieval (inspired by `session-search`)

Q06. Given a known requirement, can the original session ID and message or line be retrieved, with its timestamp and source?  
Q07. Can the system distinguish an indexed summary, a retrievable transcript, and an irrecoverably missing transcript?  
Q08. When the index is stale, does the result disclose freshness and refuse to claim coverage of later sessions?  
Q09. Can a bounded quotation prove the answer without loading or leaking the whole conversation?  
Q10. In matched fixtures with similar project names or repeated terms, what are retrieval precision and missed-source counts?

## C. Source provenance (inspired by `memory-bridge`)

Q11. Does each reusable lesson identify its original source and the agent/tool that produced it?  
Q12. Can a reviewer distinguish an independently observed tool result from a summary derived from another assistant?  
Q13. When two agents repeat the same unsupported claim, does the system avoid counting this as independent confirmation?  
Q14. If a source or manifest entry is absent, does output say `unknown` and name the missing evidence?  
Q15. Can a source conflict be displayed without overwriting an earlier observation or silently choosing one?

## D. Relation quality (inspired by `cross-linker`)

Q16. Can a decision link to exact task, source, plan revision, affected file, and receipt IDs without guessing an edge?  
Q17. Which links are direct source observations and which are only candidates inferred from text or tags?  
Q18. Can an incorrect inferred edge be rejected without mutating the original source or audit trail?  
Q19. Do fixtures catch superseded decisions, duplicate lessons, contradictory claims, and orphaned references?  
Q20. Can the review report relationship false positives separately from true origin matches?

## E. Recovery principles (inspired by `wiki-rebuild`)

Q21. Is an actual Obsidian knowledge vault present, or is the problem retrieval from Git/events/chats rather than a wiki rebuild?  
Q22. If data is missing, what is the least destructive existing recovery method before discussing a full re-ingest?  
Q23. If an archive is considered, how would integrity and recovery to a temporary destination be verified first?  
Q24. How does recovery preserve original provenance, revision history, and known unrecoverable gaps?  
Q25. What interrupted-operation and rollback fixtures would be necessary before authorizing any future write operation?

## F. Evidence boundaries and adoption decision

Q26. Can an index, linked note, or user-supplied `verified` field ever be mistaken for a Build Admission or verification receipt? Show the denying rule.  
Q27. Can exact source/revision bindings be represented using current contracts and stores without altering stage ownership?  
Q28. Who is authorized to read, retain, export, or delete raw conversations, code, and trace evidence? Which sensitive fields are excluded?  
Q29. What deterministic fixture suite distinguishes valid provenance, false matches, stale indexes, missing transcripts, conflicting sources, and unauthorized promotion?  
Q30. What measured improvement over existing search and logs would justify adopting each candidate; which ones should be rejected as redundant?

## Deferred evaluation instructions

Inspect the target repository and its actual bootstrap instructions before any tool execution. Build an evidence inventory before design proposals. Use read-only probes and labeled matched fixtures. Report observed results and unresolved gaps, separating facts, hypotheses, and proposed changes. Do not install or run `wiki-rebuild`, change Runtime contracts, create competing memory storage, infer approvals, or claim E2E validation without actual execution.

See [TRACE-REVIEW.md](TRACE-REVIEW.md) for the review boundary and [EXTRACTION.md](EXTRACTION.md) for pinned upstream sources.
