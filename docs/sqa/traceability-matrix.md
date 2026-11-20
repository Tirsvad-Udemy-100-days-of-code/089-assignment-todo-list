# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [a3a64c5] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | SA-001, PP-001 | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | BC-001 | PP-001 | [RC-002] |
| [PP-001] | Project Plan | en | it | BC-001, SA-001 | MIL-001 to MIL-006 | [RC-003] |
| [MIL-001] | Milestone | en | it | BC-001 | - | [RC-004] |
| [MIL-002] | Milestone | en | it | BC-001 | - | [RC-005] |
| [MIL-003] | Milestone | en | it | BC-001 | - | [RC-006] |
| [MIL-004] | Milestone | en | it | BC-001 | - | [RC-007] |
| [MIL-005] | Milestone | en | it | BC-001 | - | [RC-008] |
| [MIL-006] | Milestone | en | it | BC-001 | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | - | ADR-0001 (planned) | - | Gap |
| CN-002 | - | ADR-0001 (planned) | - | Gap |
| CN-003 | - | ADR-0001 (planned) | - | Gap |
| CN-004 | - | ADR-0001 (planned) | - | Gap |
| CN-005 | - | ADR-0001 (planned) | - | Gap |
| CN-006 | - | ADR-0001 (planned) | - | Gap |
| CN-007 | - | ADR-0001 (planned) | - | Gap |
| CN-008 | - | ADR-0001 (planned) | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- No views, ADR or test plan exist yet; concerns are `Gap` until MIL-001 to MIL-006 deliver them.
- `-` in Upstream means foundational; in Downstream nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-domain-storage.md
[MIL-003]: ../milestones/mil-003-http-api.md
[MIL-004]: ../milestones/mil-004-kanban-board-ui.md
[MIL-005]: ../milestones/mil-005-card-details.md
[MIL-006]: ../milestones/mil-006-wiki-release.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-mil-005.md
[RC-009]: ./reviews/rc-009-mil-006.md
[a3a64c5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/commit/a3a64c5ad7831b1e3ad88ecf9902ebcf6f2f0d16
