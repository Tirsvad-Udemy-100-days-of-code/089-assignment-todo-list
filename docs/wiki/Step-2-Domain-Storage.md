**English** · [Dansk](Step-2-Domain-Storage-da) · [Bahasa Malaysia](Step-2-Domain-Storage-ms)

# Step 2: Domain and storage

![Step 2: the board read from SQLite](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-02.png)

## What we built

The core rules of the board and their storage. The page now reads a board from a SQLite file and shows the five default lists with their cards.

## The domain model

| Concept | Fields | Rules |
| --- | --- | --- |
| Board | id, name | A new store gets one board with the lists Backlog, To Do, In Progress, Review and Done |
| List | id, board, name, position | Lists are ordered left to right; positions have no gaps |
| Card | id, list, title, position | Cards are ordered top to bottom; a card is in exactly one list |

Use cases: get the board, create, rename, delete and move a list, and create, rename, delete and move a card. A name is trimmed, must not be empty and has at most 100 characters.

## What we gained

- **Entities.** Small frozen dataclasses (`Board`, `CardList`, `Card`) hold the data; the list class is called `CardList` because `list` is a Python builtin.
- **A port.** `BoardRepository` is a `Protocol` in the domain; the application depends on it, not on SQLite.
- **Use cases.** One small class per thing a user can do, with one `execute` method.
- **An adapter.** `SqliteBoardRepository` implements the port with the standard `sqlite3` module, parameterised queries and a transaction per call.
- **Two kinds of tests.** Unit tests use an in-memory fake; integration tests run the real adapter on a temporary file. Coverage is 99 percent.
- **Positions without gaps.** Moving or deleting renumbers the neighbours in the same transaction.
