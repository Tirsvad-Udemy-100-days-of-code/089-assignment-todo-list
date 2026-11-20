# ADR-0001: Standard-library stack

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Kanban todo list must run for S02 and S03 without installing runtime
packages ([BC-001] constraint, concern CN-007 in [SA-001]). It needs a web
server, a database, a page that updates without reload, and an architecture a
learner can read.

Options evaluated:

1. A web framework (Flask or FastAPI) with an ORM. Fast to write, but adds
   runtime dependencies and hides the HTTP and SQL that the exercise teaches.
2. The Python standard library: `http.server` for HTTP, `sqlite3` for storage
   and plain JavaScript in the browser. More code, no dependencies.
3. A single-page application with a JavaScript build tool. Adds a second
   toolchain and Node as a requirement.

Forces: no runtime dependencies, readable code, single user, small scope,
Python 3.13 or newer.

## Decision

Use option 2: `http.server`, `sqlite3` and plain JavaScript, with an MVC
presentation layer over a clean-architecture core (domain, application,
infrastructure, presentation). Development tools (pytest, ruff, mypy) stay in
an optional `dev` group.

## Consequences

**Positive:**

- The runtime dependency list is empty; setup is a virtual environment and one command.
- Every layer is visible and testable; the standard-library server shows how HTTP works.
- The database sits behind a port, so another store can replace SQLite.

**Negative:**

- More code than a framework (a small router, JSON handling, validation).
- `http.server` is not meant for heavy load; the scope is one user on one machine.
- Plain JavaScript drag and drop needs its own tests.

## Affected Artifacts

- [BC-001]
- [SA-001]

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
