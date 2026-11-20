# Business Case: Kanban Todo List

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 89 of the 100 Days of Code bootcamp asks the participant to build a todo
list website. The Product Owner chooses the ambitious form: a Kanban task board
in the style of Trello, with boards, lists and cards that can be added, edited,
moved by drag and drop and removed. The result is a small, readable Python
project that runs from the standard library alone, is documented in three
languages, and shows each build step with a screenshot. It serves as a
portfolio piece for interviews and as a reference other course participants
can read and run.

## Methodological and Standards Foundation

- Methodology: Larman, *Applying UML and Patterns*, for the domain model and
  use cases; Clean Architecture for the layers; MVC for the web presentation.
- Quality standard: ISO/IEC 25010:2023 characteristics tag every QC criterion.
- Process: the project's SQA and QC framework (plan first, review each artifact,
  one pull request per milestone).
- Code: Python 3.13 or newer, pytest, doxygen comments, constants kept in
  `constants.py`.

## Problem Statement

1. A todo list is a rite of passage for a developer, but a plain list of items
   shows little skill. Interviewers, who are often managers, work daily in task
   boards such as Trello or Jira and judge a task board quickly.
2. Course solutions are often a single file with no tests, no setup guide and no
   explanation of what was learned, so they are hard to run and hard to learn from.
3. The belief that would kill the idea if false: a Kanban board can be built
   with the Python standard library alone and still be pleasant to use. If a
   framework is needed to make it usable, the "no runtime dependencies"
   promise to S03 breaks.

## Business Opportunity

A finished, tested and documented Kanban board gives S01 a concrete artifact to
show in interviews, gives S02 a clear solution to compare with their own, and
gives S03 a repository with ideas that runs with one command and no installs.

## Objectives

1. Deliver a web Kanban board with boards, lists and cards, stored persistently.
2. Let a user add, rename, move (drag and drop) and delete lists and cards, and
   give a card a coloured label, a description, a due date, a done state and
   comments. A new board starts with the lists Backlog, To Do, In Progress,
   Review and Done.
3. Ship it with no runtime dependencies, tests with pytest, and doxygen
   comments in the source.
4. Document how to create and use a local `.venv`, run the project and run the
   tests, in the README.
5. Show every build step with a screenshot in the README and in the wiki, and
   explain in the wiki what each step taught, in English, Danish and Bahasa Malaysia.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- A single-user Kanban web application in the look of the Product Owner's
  sketch (a Trello-style board): five default lists named Backlog, To Do, In
  Progress, Review and Done, cards with coloured labels, a description
  indicator and a comment count, an "Add a card" control under each list,
  drag and drop, and card details (description, due date, done, comments).
- A wireframe of the board drawn for this project from the sketch, kept in
  `docs/wireframes/`.
- A JSON API behind the web page, with the assignment's wording for names
  (board, list, card).
- Persistence in a local SQLite file.
- Unit, integration and browser tests; the browser tests and the screenshots run
  in a Docker container.
- README from the framework template; wiki in three languages; Doxyfile;
  `pyproject.toml`; Python `.gitignore`; a static code scan with opengrep before
  every push.
- Repository description and topics on the git host.

### Out of Scope

- User accounts, sign-in and multi-user sharing.
- Real-time collaboration, notifications, file attachments and workspaces beyond a single board view.
- Deployment to a public server and any paid service.
- Mobile applications.
- Third-party runtime packages.

## Expected Benefits

### Tangible Benefits

- A runnable portfolio project with a passing test suite.
- A README and a three-language wiki that a newcomer can follow without help.
- Screenshots that prove each step works.

### Intangible Benefits

- Practice in planning, layering and testing a complete web application.
- A written reflection that helps the next project.

## Strategic Alignment

The project completes Day 89 of the bootcamp and supports the participant's
goal of a strong interview portfolio. It follows the framework's plan-first
workflow, so the repository also demonstrates process, not only code.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Board features work | All of create, rename, move, delete for lists and cards pass an end-to-end test | Browser test in a container exits 0 |
| 2 | Tests | At least 90 percent line coverage of `src/` measured on the unit and integration tests | pytest run with the coverage report of the project's dev tools |
| 3 | No runtime dependencies | 0 packages in `[project].dependencies` | Inspect `pyproject.toml` |
| 4 | Setup works from the README | A fresh clone reaches a running board in 5 commands or fewer | Follow the README in a clean container |
| 5 | Screenshots | One screenshot per milestone (6) in the README and in every wiki language | Count image links |
| 6 | Wiki languages | 3 languages with the same page set | Page list of `docs/wiki/` |
| 7 | Static scan | 0 findings of severity error from opengrep at each push | Scan output |
| 8 | Repository metadata | Description and at least 5 topics set | Read back from the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Drag and drop with plain JavaScript is harder than expected | Schedule slip on the board milestone | Use the browser's native drag and drop events; fall back to move buttons if the test is unstable |
| Standard-library HTTP server is minimal | Fragile routing and limited concurrency | Keep one small router in the presentation layer; single-user scope makes this acceptable |
| Screenshots need a browser and the host desktop must not be used | Screenshots not produced | Headless browser in a Docker container; stop and report if Docker is unavailable |
| Tokens in `.env` leak into the repository | Security defect | `.env` is ignored, never imported, never printed; opengrep scan before each push |
| Wiki translations drift from English | Inconsistent documentation | English is written first; the page set is checked equal across languages |

## Assumptions

- S01 is the Product Owner, developer and reviewer, and reachable in chat.
- S02 and S03 are reached only through the published repository.
- The git host `git.tirsystem.com` accepts the tokens in `.env`, and the
  repository already exists under the organization `Tirsvad-Udemy-100-days-of-code`.
- Docker is available on the development machine.
- The wiki is enabled in the repository settings.

## Constraints

- Python 3.13 or newer; a local `.venv`; pytest; constants in `constants.py`.
- Folders `src/`, `tests/` and `docs/`.
- No runtime dependencies unless needed; none are expected.
- The text "AI" does not appear in any artifact of the repository.
- Duration: finish by 2026-12-04, about 200 minutes of course effort plus
  documentation work.
- Tokens come from `.env` for personal use only; they are not imported, tested
  or committed.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 40 hours of S01's time across the plan, including documentation and translation | A portfolio-grade project, a reference for S02, a repository of ideas for S03 |
| No licences or hosting fees | No recurring cost |

The assessment is qualitative because the project is a learning exercise with
no revenue.

## Stakeholders

| ID | Role in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer |
| S02 | Udemy participants who compare solutions |
| S03 | Repository viewers who look for ideas |

The roles, power and interest of each are in [SA-001].

## Recommendation

Proceed.

---

[SA-001]: ./stakeholder-analysis.md
