# Project Plan

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This plan schedules the six build steps of the Kanban todo list over the Business
Case constraint: finish by 2026-12-04. Each step is one gateway, one branch and
one pull request, and each ends with a screenshot and wiki pages.

## Planning Assumptions

- Week 1 starts 2026-11-23; the plan ends by 2026-12-04, per [BC-001].
- Phase length: one to three days; the pace follows the communication cadence in [SA-001].
- Branches are named for the milestone, for example `mil-001-foundation`, and each pull request closes its issues.
- The PO language is English and the domain is IT; the wiki adds Danish and Bahasa Malaysia.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project foundation | [MIL-001] | 2026-11-23 to 2026-11-25 | 2026-11-25 | S01 | none | Tooling, README, skeleton, first page | |
| Domain and storage | [MIL-002] | 2026-11-25 to 2026-11-27 | 2026-11-27 | S01 | none | Entities, SQLite repository, read-only board | |
| JSON API and editing | [MIL-003] | 2026-11-27 to 2026-11-30 | 2026-11-30 | S01 | none | API and edit controls | |
| Kanban board and drag and drop | [MIL-004] | 2026-11-30 to 2026-12-02 | 2026-12-02 | S01 | none | Styled board with drag and drop | |
| Card details | [MIL-005] | 2026-12-02 to 2026-12-03 | 2026-12-03 | S01 | none | Labels, description, due date, done state, comments | |
| Wiki, reflection and release | [MIL-006] | 2026-12-03 to 2026-12-04 | 2026-12-04 | S01 | none | Three-language wiki, reflection, final checks | |

```plantuml
@startgantt
Project starts 2026-11-23
[Project foundation] starts 2026-11-23 and ends 2026-11-25
[Domain and storage] starts 2026-11-25 and ends 2026-11-27
[JSON API and editing] starts 2026-11-27 and ends 2026-11-30
[Kanban board and drag and drop] starts 2026-11-30 and ends 2026-12-02
[Card details] starts 2026-12-02 and ends 2026-12-03
[Wiki, reflection and release] starts 2026-12-03 and ends 2026-12-04
[Foundation Go/No-Go] happens 2026-11-25
[Domain Go/No-Go] happens 2026-11-27
[API Go/No-Go] happens 2026-11-30
[Board Go/No-Go] happens 2026-12-02
[Details Go/No-Go] happens 2026-12-03
[Release Go/No-Go] happens 2026-12-04
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Boards, the five default lists, cards, persistent storage | [MIL-002] |
| JSON API and editing | [MIL-003] |
| Drag and drop | [MIL-004] |
| Card details (labels, description, due date, done, comments) | [MIL-005] |
| Tests, README, Doxyfile, `pyproject.toml`, `.gitignore`, opengrep, repository metadata | [MIL-001] |
| Screenshots per step | [MIL-001] to [MIL-005] |
| Wiki in three languages, reflection | [MIL-001] to [MIL-006] |

## Dependencies

```
MIL-001 → MIL-002 → MIL-003 → MIL-004 → MIL-005 → MIL-006
```

A No-Go moves every later decision date by the days needed to fix and review again;
the end date of 2026-12-04 is reported as at risk in the run summary.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Docker browser harness takes longer than planned | Screenshots late in every milestone | Build it first in [MIL-001]; stop and report if Docker is unavailable |
| Wiki translation in three languages grows | Release milestone slips | Write each step's wiki pages in the same milestone, not at the end |
| The repository host API rejects a token | Metadata or pull requests blocked | Stop and report; the token is never printed |

## Open Issues

- No Domain Dictionary (`DICT`) or Governance document exists; the vocabulary is small and every owner is S01, so neither is needed at this size.
- The PlantUML server setting in `docs/artifact-registry.md` is empty, so the Gantt chart is not rendered by the check script.
- The framework's prompt-log folder `docs/ai-prompts/` carries a name the Product Owner forbids in artifacts; it is kept out of the repository through `.gitignore`.
- `requires-python` is set to 3.13 or newer; the installed interpreter is 3.13.14.
- The dry-run output of `sync-project.sh` is the plan the Product Owner accepts; `--apply` runs after acceptance, because the publish workflow is not installed.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-foundation.md
[MIL-002]: ./milestones/mil-002-domain-storage.md
[MIL-003]: ./milestones/mil-003-http-api.md
[MIL-004]: ./milestones/mil-004-kanban-board-ui.md
[MIL-005]: ./milestones/mil-005-card-details.md
[MIL-006]: ./milestones/mil-006-wiki-release.md
