# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [a3a64c5] |

---

## Purpose

This analysis names the people the Kanban todo list serves, how much power and
interest each has, and what each expects. It follows the power/interest grid
and maps each concern to a FURPS+ attribute so the plan can answer it.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A working, tested Kanban board that impresses an interviewer |
| S02 | Udemy participants | Course participants who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's names and README instructions |
| S03 | Repository viewers | Visitors who browse the repository for ideas | GitHub and Gitea community | LOW | MEDIUM | Monitor | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews every artifact and accepts the plan.
- **Keep Informed (S02):** cannot change the project but depends on its clarity.
  They get the README and wiki.
- **Monitor (S03):** casual visitors; the repository description, topics and
  README serve them without further contact.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The board must support lists, cards and drag and drop | Functionality |
| CN-002 | S01 | Tests and quality checks must give confidence before every push | Reliability |
| CN-003 | S01 | Progress must be traceable through branches and pull requests | Supportability |
| CN-004 | S02 | The code must be readable and use the assignment's names | Supportability |
| CN-005 | S02 | A newcomer must be able to run the project and its tests from the README | Usability |
| CN-006 | S03 | The repository must have a clear description, topics and README | Usability |
| CN-007 | S03 | The project must not require installing runtime packages | Implementation constraint |
| CN-008 | S02 | Every build step must be shown by a screenshot and explained in the wiki, in English, Danish and Bahasa Malaysia | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan; run summary | All |
| COM-002 | Pull request description | One per milestone | Changes and closed issues | MIL-001 to MIL-006 |
| COM-003 | README and wiki | Updated every milestone | Instructions, screenshots, lessons | MIL-001 to MIL-006 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| A richer board (more features) versus no runtime dependencies | S01, S03 | Use only browser and standard-library features; cut features that need a package |
| Three-language wiki effort versus delivery date | S01, S02 | English first; translations follow page by page within the same milestone |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objectives 1 and 2 of [BC-001] |
| S01 | CN-002, CN-003 | Objective 3 of [BC-001] |
| S02 | CN-004, CN-005 | Objectives 3 and 4 of [BC-001] |
| S02 | CN-008 | Objective 5 of [BC-001] |
| S03 | CN-006 | Objective 6 of [BC-001] |
| S03 | CN-007 | Objective 3 of [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | pending review | |

---

[BC-001]: ./business-case.md
[a3a64c5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/commit/a3a64c5ad7831b1e3ad88ecf9902ebcf6f2f0d16
