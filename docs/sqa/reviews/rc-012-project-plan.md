# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Review of PP-001 | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions: start 2026-11-23, end 2026-12-04, per BC-001 constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Pass |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the target dates in each MIL and fall inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-006 is acyclic and matches the schedule. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section says a No-Go moves later dates and the end date is reported at risk. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | N-A | No governance document exists; every owner and reviewer is S01 and no role name is invented. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions state their source. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with mitigation. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Pass |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none for every gateway; no user stories exist. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars and table agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column is blank until the sync, as the framework says. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One plan, Version History kept. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells are English; S01 confirmed English as the PO language in chat and accepted the plan in chat on 2026-11-20. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Domain terms board, list, card, label, comment are used consistently, no synonyms. No Domain Dictionary document exists yet; that is recorded in the Project Plan Open Issues as not needed for this size. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Checked on the document; English, IT executive or professional register as the registry states. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 (competent in the IT domain and English) confirmed the content by accepting the plan in chat on 2026-11-20. Stand-in decision, not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Abbreviations such as API, JSON, MVC, SVG are used without being spelled out. Optional criterion; non-blocking. |

## Overall Verdict

Go (re-review after a wording change) — no Mandatory criterion fails; the only Fail is Optional and non-blocking. Reviewer is the stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Spell out API, JSON, MVC and SVG on first use, or add a short glossary to the README | S01 | 2026-12-04 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
