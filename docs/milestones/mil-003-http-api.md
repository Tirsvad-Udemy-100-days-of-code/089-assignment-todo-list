# Milestone 3: JSON API and editing

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether a user can change the board through the browser and the API.

## Deliverable

A JSON API for boards, lists and cards, forms or controls on the page to add, rename and delete lists and cards, tests of the API and the step 3 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | API routes create, read, rename and delete lists and cards and return correct status codes | Met | Not met: fix and review again |
| 2 | Invalid input returns a 400 with a message and never a stack trace | Met | Not met: fix and review again |
| 3 | Added items survive a server restart | Met | Not met: fix and review again |
| 4 | Browser test in a container adds a list and a card | Met | Not met: fix and review again |
| 5 | `docs/screenshots/step-03.png` exists and is shown in the README and the wiki | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Domain, storage and the board page |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 | [BC-001] |
| CN-001 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-30 — after MIL-002 and inside the plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the small router | Add a router in the presentation layer that maps method and path to controller functions, serves static files and returns JSON, using only `http.server`. | No |  |
| 2 | Implement list endpoints | Add create, rename and delete endpoints for lists with validation errors returned as JSON and tested with the standard-library HTTP client. | No |  |
| 3 | Implement card endpoints | Add create, rename and delete endpoints for cards, with the same validation and tests. | No |  |
| 4 | Add editing controls to the page | Add plain JavaScript that calls the API to add a list, add a card, rename and delete, and redraws the board without a full reload. | No |  |
| 5 | Add browser test in a container | Add an end-to-end test that adds a list and a card in a headless browser. Environment: Docker container, results written as files. | No |  |
| 6 | Capture step screenshot for step 3 | Capture `docs/screenshots/step-03.png` showing an edited board and add it to the README. | No |  |
| 7 | Write wiki pages for step 3 | Write the three-language wiki pages on routing, HTTP status codes and JSON, with the screenshot. | No |  |

---

[BC-001]: ../business-case.md
