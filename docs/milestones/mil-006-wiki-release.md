# Milestone 6: Wiki, reflection and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project is complete, documented and ready for S02 and S03.

## Deliverable

A complete three-language wiki with a sidebar, the reflection, a final README, Doxygen output check, a full scan and run summary, and the repository released.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki has the same page set in English, Danish and Bahasa Malaysia, with sidebar and language lines | Met | Not met: fix and review again |
| 2 | Every milestone's screenshot is in the README and the wiki | Met | Not met: fix and review again |
| 3 | The README reflection answers the assignment's questions | Met | Not met: fix and review again |
| 4 | Opengrep, pytest and the container browser test pass on `main` | Met | Not met: fix and review again |
| 5 | No file in the repository contains the standalone word for artificial intelligence as a term | Met | Not met: fix and review again |
| 6 | Repository description and topics are present on the host | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | Complete application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4, 5 and 6 | [BC-001] |
| CN-005, CN-006, CN-008 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-12-04 — the end of the plan window in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write wiki home and sidebar | Create `Home`, `_Sidebar` and the page index in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) following `framework/process/wiki.md`. | No |  |
| 2 | Complete the step pages | Check that each milestone page exists in all three languages and explains what was gained, with its screenshot. | No |  |
| 3 | Write the reflection | Write the assignment's reflection (approach, what was hard and easy, biggest learning, what to do differently) in the README and the wiki. | No |  |
| 4 | Finalize the README | Check the setup and run instructions in a clean container, the gallery with six screenshots and the project documents appendix. | No |  |
| 5 | Run the full quality pass | Run pytest, coverage, the container browser test, doxygen and opengrep, and the framework checks; fix findings. | No |  |
| 6 | Verify repository metadata and wording | Read the description and topics back from the host and search the repository for the forbidden wording. | No |  |

---

[BC-001]: ../business-case.md
