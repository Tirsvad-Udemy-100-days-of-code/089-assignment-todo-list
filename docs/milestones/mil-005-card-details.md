# Milestone 5: Card details

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether a card carries what a task manager needs: description, due date and done state.

## Deliverable

A card detail dialog with coloured label, description, due date, done toggle and comments, a label bar, description icon and comment count on each card, overdue and done marking, tests and the step 5 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A card stores label, description, due date, done state and comments across reloads | Met | Not met: fix and review again |
| 2 | An invalid due date is rejected with a 400 | Met | Not met: fix and review again |
| 3 | Overdue cards are marked and done cards are crossed out | Met | Not met: fix and review again |
| 4 | Coverage of `src/` is at least 90 percent | Met | Not met: fix and review again |
| 5 | `docs/screenshots/step-05.png` exists and is shown in the README and the wiki | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The Kanban board |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2 | [BC-001] |
| Success criterion 2 | [BC-001] |
| CN-001 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-03 — after MIL-004 and inside the plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add card detail fields | Add label colour, description, due date, done state and a list of text comments to the card use cases, repository schema migration and API, with tests. | No |  |
| 2 | Build the card detail dialog | Open a dialog from a card to edit the details and save through the API, using a native `dialog` element. | No |  |
| 3 | Mark overdue and done cards | Show a coloured label bar, a description icon, a comment count and a due date badge on each card, mark overdue cards and cross out done cards. | No |  |
| 4 | Close test gaps | Run coverage, add missing tests until at least 90 percent of `src/` is covered, and run the full browser test. | No |  |
| 5 | Capture step screenshot for step 5 | Capture `docs/screenshots/step-05.png` with the dialog open and add it to the README. | No |  |
| 6 | Write wiki pages for step 5 | Write the three-language wiki pages on data modelling, validation and dates, with the screenshot. | No |  |

---

[BC-001]: ../business-case.md
