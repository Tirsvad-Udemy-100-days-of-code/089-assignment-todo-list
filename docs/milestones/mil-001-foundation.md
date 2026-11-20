# Milestone 1: Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the repository, tooling and a first running page are in place so that every later milestone can build on them.

## Deliverable

A configured repository (description, topics, `pyproject.toml`, `.gitignore`, `.editorconfig`, `constants.py`, `Doxyfile`), a README with venv instructions, a layered `src/` skeleton that serves a first page, a passing pytest run, the opengrep helper, the screenshot harness and the step 1 screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes in a fresh `.venv` | Met | Not met: fix and review again |
| 2 | `pyproject.toml` requires Python 3.13 or newer and lists no runtime dependencies | Met | Not met: fix and review again |
| 3 | `doxygen Doxyfile` runs with no warnings | Met | Not met: fix and review again |
| 4 | The README explains creating `.venv`, `python -m pip install --upgrade pip`, running and testing | Met | Not met: fix and review again |
| 5 | Repository description and at least 5 topics are set on the git host | Met | Not met: fix and review again |
| 6 | Opengrep reports no error-severity finding | Met | Not met: fix and review again |
| 7 | `docs/screenshots/step-01.png` exists and is shown in the README | Met | Not met: fix and review again |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001 | Scope and constraints |
| SA-001 | Stakeholder IDs for ownership |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3, 4 and 6 | [BC-001] |
| Success criteria 3, 4, 7, 8 | [BC-001] |
| CN-005, CN-006, CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-25 — inside the plan window ending 2026-12-04 in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Read `TOKEN_FOR_GITEA_REPO` from `.env` at run time only (never imported into the project, never printed) and set the repository description and topics through the Gitea API, then read them back. Serves CN-006 of the Stakeholder Analysis. | No |  |
| 2 | Add Python project configuration | Create `pyproject.toml` (Python 3.13 or newer, no runtime dependencies, pytest as an optional dev dependency, pytest settings), a Python `.gitignore` that also ignores `.env` and `.venv`, and `.editorconfig` from the framework baseline; check it with `check-editorconfig.sh`. | No |  |
| 3 | Add constants module and Doxyfile | Create `src/todo_list/constants.py` as the only home of constants (host, port, database file name, titles) and a `Doxyfile` for doxygen comments in the source; the source uses doxygen comment style from the first file on. | No |  |
| 4 | Write README with venv instructions | Create `README.md` from the framework template: overview, requirements, creating and using a local `.venv`, `python -m pip install --upgrade pip`, installing the dev dependency, running the app and the tests, and a screenshot gallery. | No |  |
| 5 | Record stack decision as an ADR | Write ADR-0001: standard-library `http.server`, `sqlite3` and plain JavaScript, no framework, MVC presentation over a clean-architecture core. Reason: the no-runtime-dependency promise to S03 (CN-007). | No |  |
| 6 | Create layered skeleton and first page | Create `src/todo_list/` with `domain`, `application`, `infrastructure` and `presentation` packages, a composition root and a first page that returns a titled board shell, with a pytest test. | No |  |
| 7 | Add opengrep helper | Add a script that runs `~\.opengrep\cli\latest\opengrep.exe` over `src/` and `tests/` and fails on error-severity findings; document that it runs before every push to Gitea. | No |  |
| 8 | Build screenshot harness in Docker | Build a Docker container with a headless browser that starts the app, opens a page and writes a PNG to `docs/screenshots/`. Environment: Docker container, never the host desktop (`framework/process/gui-testing.md`). | No |  |
| 9 | Capture step screenshot for step 1 | Run the harness for the first page and save `docs/screenshots/step-01.png`; show it in the README. | No |  |
| 10 | Write wiki pages for step 1 | Write the English, Danish and Bahasa Malaysia wiki pages explaining what step 1 taught (venv, pyproject, constants, doxygen, project layout), with the screenshot. | No |  |

---

[BC-001]: ../business-case.md
