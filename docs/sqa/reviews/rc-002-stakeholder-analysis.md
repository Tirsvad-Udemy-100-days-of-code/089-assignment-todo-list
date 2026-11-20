# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Review of SA-001 | [a3a64c5] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: S01 (reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01, S02, S03 all have power, interest and quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | IDs S01 to S03, never reused. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Role, organization, Power and Interest are table columns. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | COM-001 to COM-003 map to milestones. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Two conflicts, each with a mitigation. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | Business Goal Alignment table cites BC-001 objectives. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concern register maps each concern to a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short rows in plain language. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-008, each with its stakeholder. |

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

Go — no Mandatory criterion fails; the only Fail is Optional and non-blocking. Reviewer is the stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Spell out API, JSON, MVC and SVG on first use, or add a short glossary to the README | S01 | 2026-12-04 |

---

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[a3a64c5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/commit/a3a64c5ad7831b1e3ad88ecf9902ebcf6f2f0d16
