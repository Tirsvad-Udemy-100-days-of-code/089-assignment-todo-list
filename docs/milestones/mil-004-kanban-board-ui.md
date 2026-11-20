# Milestone 4: Kanban board and drag and drop

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the board behaves like a Kanban board: cards move between and within lists.

## Deliverable

A styled Kanban board where cards and lists are reordered by drag and drop, persisted through a move endpoint, tested end to end, with the step 4 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A move endpoint changes list and position and renumbers positions without gaps | Met | Not met: fix and review again |
| 2 | A card dragged to another list is still there after reload | Met | Not met: fix and review again |
| 3 | A card dragged within a list keeps the new order after reload | Met | Not met: fix and review again |
| 4 | Layout works at 1280 and 400 pixel widths | Met | Not met: fix and review again |
| 5 | `docs/screenshots/step-04.png` exists and is shown in the README and the wiki | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | API and editing controls |

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

2026-12-02 — after MIL-003 and inside the plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the move use case and endpoint | Add the use case and endpoint that move a card to a list and position, and move a list, renumbering positions, with unit and API tests. | No |  |
| 2 | Add drag and drop in the browser | Use the browser's native drag and drop events to move cards and lists and call the move endpoint, with move buttons as the fallback if drag events are unstable. | No |  |
| 3 | Draw the wireframe | Draw a wireframe of the board from the Product Owner’s sketch (blue background, five rounded list columns, white cards, an Add a card control under each list) as an SVG in `docs/wireframes/`, kept with the use case it illustrates. | No |  |
| 4 | Style the board | Add a stylesheet that follows the wireframe: Kanban columns, cards, hover and drag states, readable at narrow widths, and no external fonts or libraries. | No |  |
| 5 | Add end-to-end drag test | Test in a headless browser in a Docker container that a card dragged across lists persists after reload. | No |  |
| 6 | Capture step screenshot for step 4 | Capture `docs/screenshots/step-04.png` showing a board with cards in several lists and add it to the README. | No |  |
| 7 | Write wiki pages for step 4 | Write the three-language wiki pages about the drag and drop events, ordering and what was hard. | No |  |

---

[BC-001]: ../business-case.md
