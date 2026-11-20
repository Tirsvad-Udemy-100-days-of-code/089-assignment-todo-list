# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [SRC-MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Review of SRC-MIL-004 | [515c6da] |

---

## Artifact Under Review

- Instance reviewed: [SRC-MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of src/ and tests/ of milestone 4
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff N rules pass; modules snake_case, classes PascalCase, constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (render_board_page, BoardController, HttpResponse). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` and `ruff check` pass; one explained noqa (N802, name fixed by the standard library). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes; every signature annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Router catches only BadRequestError, InvalidNameError and NotFoundError and maps them to status codes; json errors are re-raised with `from`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; the only builtin-like name is `format`, fixed by the base class signature. |
| 7 | Files, locks and connections are managed with context managers | Pass | SQLite connections are closed with `closing` and committed with `with`; the server is closed in `finally`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | All public modules, classes and functions have doxygen docstrings; `doxygen Doxyfile` is silent. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` is used; nothing sensitive is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No DCD artifact exists; the milestone task is a plain task. The domain model and use case list are in the step 2 wiki pages. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 77 host tests and 11 container browser tests, named for behaviour, independent; 99.8 percent coverage of src/. The JavaScript is covered by the browser tests only. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` configured in pyproject.toml and clean. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; dev tools declared with lower bounds. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Error-to-status mapping only in Router._call; field checks only in require_str and require_int; routes only in routes.py; constants in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports only the standard library and constants.py; application imports domain; infrastructure imports domain; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Controllers, router, routes and server each have one job; controllers receive their use cases in the constructor; new routes are added in routes.py without editing the router. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Packages domain, application, infrastructure, presentation and tests/unit, integration, e2e exist. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English snake_case; README.md and LICENSE are exceptions. |

## Overall Verdict

Go — all Mandatory criteria pass or are N-A with a reason. Reviewer is the stand-in for S01, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| none | S01 | - |

---

[SRC-MIL-004]: ../../../src/todo_list
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[515c6da]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/commit/515c6daedd4edf53d3d35ec8631eee8bceab7986
