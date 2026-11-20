# Milestone 2: Domain and storage

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the core rules (board, list, card) and their persistence work independently of the web layer.

## Deliverable

Domain entities and use cases for boards, lists and cards, a SQLite repository behind a port, a board seeded with the five default lists (Backlog, To Do, In Progress, Review, Done), a read-only board page and the step 2 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Domain and application code import nothing from `infrastructure` or `presentation` | Met | Not met: fix and review again |
| 2 | Unit tests cover create, rename, reorder and delete of lists and cards | Met | Not met: fix and review again |
| 3 | Integration tests run the repository against a temporary SQLite file | Met | Not met: fix and review again |
| 4 | The board page shows the five default lists in order, Backlog first, with seeded cards | Met | Not met: fix and review again |
| 5 | `docs/screenshots/step-02.png` exists and is shown in the README and the wiki | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Tooling, skeleton and screenshot harness |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 | [BC-001] |
| CN-001, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-27 — after MIL-001 and inside the plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Model the domain | Write the domain model for board, list, card and label (name, position, colour, description, due date, done) and comment with the assignment's names, and the use case list the next milestones deliver. Names follow the PO terms. | No |  |
| 2 | Implement entities and use cases | Implement the entities and application use cases (create, rename, move, delete) with doxygen comments, inside the `domain` and `application` packages, with no framework imports. | No |  |
| 3 | Implement the SQLite repository | Implement the repository port and its SQLite adapter in `infrastructure`, create the schema on first start, create the default lists Backlog, To Do, In Progress, Review and Done on a new board, and keep the database file name in `constants.py`. | No |  |
| 4 | Write unit and integration tests | Test the use cases with an in-memory fake repository and the adapter against a temporary database; reach at least 90 percent coverage of `src/` so far. | No |  |
| 5 | Render the read-only board page | Serve `/` as a server-rendered page listing the seeded lists and cards, through the MVC controller and a view template written with the standard library. | No |  |
| 6 | Capture step screenshot for step 2 | Seed sample data in the container, capture `docs/screenshots/step-02.png` and add it to the README. | No |  |
| 7 | Write wiki pages for step 2 | Write the English, Danish and Bahasa Malaysia wiki pages explaining what step 2 taught (layers, ports, repository, tests) with the screenshot. | No |  |

---

[BC-001]: ../business-case.md
