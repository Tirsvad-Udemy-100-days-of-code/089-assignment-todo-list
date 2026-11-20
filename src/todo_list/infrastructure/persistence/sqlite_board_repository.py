"""@brief SQLite adapter of the board repository."""

import sqlite3
from collections.abc import Iterator
from contextlib import closing, contextmanager
from pathlib import Path
from typing import Any

from todo_list import constants
from todo_list.domain.entities.board import Board
from todo_list.domain.entities.card import Card
from todo_list.domain.entities.card_list import CardList
from todo_list.domain.entities.comment import Comment
from todo_list.domain.errors.board_errors import NotFoundError

_SCHEMA = """
CREATE TABLE IF NOT EXISTS boards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_id INTEGER NOT NULL REFERENCES boards(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    position INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL REFERENCES lists(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    position INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""

# Columns added to cards after the first release; older files get them on open.
_ADD_CARD_DETAIL_COLUMNS = (
    ("label", "ALTER TABLE cards ADD COLUMN label TEXT NOT NULL DEFAULT ''"),
    (
        "description",
        "ALTER TABLE cards ADD COLUMN description TEXT NOT NULL DEFAULT ''",
    ),
    ("due_date", "ALTER TABLE cards ADD COLUMN due_date TEXT"),
    ("done", "ALTER TABLE cards ADD COLUMN done INTEGER NOT NULL DEFAULT 0"),
)

# Must equal constants.SCHEMA_VERSION; a unit test checks it.
_SET_SCHEMA_VERSION_SQL = "PRAGMA user_version = 1"

_CARDS_OF_LIST_SQL = (
    "SELECT id, list_id, title, position, label, description, due_date, done, "
    "(SELECT COUNT(*) FROM comments WHERE comments.card_id = cards.id) FROM cards "
    "WHERE list_id = ? ORDER BY position"
)

_CARD_BY_ID_SQL = (
    "SELECT id, list_id, title, position, label, description, due_date, done, "
    "(SELECT COUNT(*) FROM comments WHERE comments.card_id = cards.id) FROM cards "
    "WHERE id = ?"
)


class SqliteBoardRepository:
    """@brief Stores boards, lists and cards in one SQLite file."""

    def __init__(self, database_path: Path) -> None:
        """@brief Open the store and create the tables if they are missing.

        @param database_path The SQLite file.
        """
        self._path = database_path
        with self._transaction() as connection:
            connection.executescript(_SCHEMA)
            _migrate(connection)

    @contextmanager
    def _transaction(self) -> Iterator[sqlite3.Connection]:
        with closing(sqlite3.connect(self._path)) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            with connection:
                yield connection

    def first_board(self) -> Board | None:
        """@brief Return the first board, or None when there is none."""
        with self._transaction() as connection:
            row = connection.execute(
                "SELECT id, name FROM boards ORDER BY id LIMIT 1"
            ).fetchone()
        return None if row is None else Board(row[0], row[1])

    def add_board(self, name: str) -> Board:
        """@brief Store a new board."""
        with self._transaction() as connection:
            cursor = connection.execute("INSERT INTO boards (name) VALUES (?)", (name,))
        return Board(_row_id(cursor), name)

    def lists_of(self, board_id: int) -> list[CardList]:
        """@brief Return the lists of a board, left to right."""
        with self._transaction() as connection:
            rows = connection.execute(
                "SELECT id, board_id, name, position FROM lists "
                "WHERE board_id = ? ORDER BY position",
                (board_id,),
            ).fetchall()
        return [CardList(*row) for row in rows]

    def cards_of(self, list_id: int) -> list[Card]:
        """@brief Return the cards of a list, top to bottom."""
        with self._transaction() as connection:
            rows = connection.execute(_CARDS_OF_LIST_SQL, (list_id,)).fetchall()
        return [_card_from_row(row) for row in rows]

    def add_list(self, board_id: int, name: str) -> CardList:
        """@brief Add a list at the right end of a board."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM boards WHERE id = ?", board_id)
            position = connection.execute(
                "SELECT COUNT(*) FROM lists WHERE board_id = ?", (board_id,)
            ).fetchone()[0]
            cursor = connection.execute(
                "INSERT INTO lists (board_id, name, position) VALUES (?, ?, ?)",
                (board_id, name, position),
            )
        return CardList(_row_id(cursor), board_id, name, position)

    def rename_list(self, list_id: int, name: str) -> CardList:
        """@brief Change the name of a list."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM lists WHERE id = ?", list_id)
            connection.execute(
                "UPDATE lists SET name = ? WHERE id = ?", (name, list_id)
            )
            return _read_list(connection, list_id)

    def delete_list(self, list_id: int) -> None:
        """@brief Delete a list and its cards."""
        with self._transaction() as connection:
            board_id = _read_list(connection, list_id).board_id
            connection.execute("DELETE FROM lists WHERE id = ?", (list_id,))
            _renumber_lists(connection, board_id, _list_ids(connection, board_id))

    def move_list(self, list_id: int, position: int) -> CardList:
        """@brief Move a list to a position on its board."""
        with self._transaction() as connection:
            board_id = _read_list(connection, list_id).board_id
            ids = [i for i in _list_ids(connection, board_id) if i != list_id]
            ids.insert(_clamp(position, len(ids)), list_id)
            _renumber_lists(connection, board_id, ids)
            return _read_list(connection, list_id)

    def add_card(self, list_id: int, title: str) -> Card:
        """@brief Add a card at the bottom of a list."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM lists WHERE id = ?", list_id)
            position = connection.execute(
                "SELECT COUNT(*) FROM cards WHERE list_id = ?", (list_id,)
            ).fetchone()[0]
            cursor = connection.execute(
                "INSERT INTO cards (list_id, title, position) VALUES (?, ?, ?)",
                (list_id, title, position),
            )
        return Card(_row_id(cursor), list_id, title, position)

    def rename_card(self, card_id: int, title: str) -> Card:
        """@brief Change the title of a card."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM cards WHERE id = ?", card_id)
            connection.execute(
                "UPDATE cards SET title = ? WHERE id = ?", (title, card_id)
            )
            return _read_card(connection, card_id)

    def delete_card(self, card_id: int) -> None:
        """@brief Delete a card."""
        with self._transaction() as connection:
            list_id = _read_card(connection, card_id).list_id
            connection.execute("DELETE FROM cards WHERE id = ?", (card_id,))
            _renumber_cards(connection, list_id, _card_ids(connection, list_id))

    def get_card(self, card_id: int) -> Card:
        """@brief Return one card."""
        with self._transaction() as connection:
            return _read_card(connection, card_id)

    def update_card_details(
        self,
        card_id: int,
        label: str,
        description: str,
        due_date: str | None,
        done: bool,
    ) -> Card:
        """@brief Replace the label, description, due date and done state."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM cards WHERE id = ?", card_id)
            connection.execute(
                "UPDATE cards SET label = ?, description = ?, due_date = ?, done = ? "
                "WHERE id = ?",
                (label, description, due_date, int(done), card_id),
            )
            return _read_card(connection, card_id)

    def add_comment(self, card_id: int, text: str, created_at: str) -> Comment:
        """@brief Add a comment to a card."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM cards WHERE id = ?", card_id)
            cursor = connection.execute(
                "INSERT INTO comments (card_id, text, created_at) VALUES (?, ?, ?)",
                (card_id, text, created_at),
            )
        return Comment(_row_id(cursor), card_id, text, created_at)

    def comments_of(self, card_id: int) -> list[Comment]:
        """@brief Return the comments of a card, oldest first."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM cards WHERE id = ?", card_id)
            rows = connection.execute(
                "SELECT id, card_id, text, created_at FROM comments "
                "WHERE card_id = ? ORDER BY id",
                (card_id,),
            ).fetchall()
        return [Comment(*row) for row in rows]

    def delete_comment(self, comment_id: int) -> None:
        """@brief Delete a comment."""
        with self._transaction() as connection:
            _require(connection, "SELECT 1 FROM comments WHERE id = ?", comment_id)
            connection.execute("DELETE FROM comments WHERE id = ?", (comment_id,))

    def move_card(self, card_id: int, list_id: int, position: int) -> Card:
        """@brief Move a card to a position in a list, possibly another list."""
        with self._transaction() as connection:
            source_id = _read_card(connection, card_id).list_id
            _require(connection, "SELECT 1 FROM lists WHERE id = ?", list_id)
            ids = [i for i in _card_ids(connection, list_id) if i != card_id]
            ids.insert(_clamp(position, len(ids)), card_id)
            _renumber_cards(connection, list_id, ids)
            if source_id != list_id:
                _renumber_cards(connection, source_id, _card_ids(connection, source_id))
            return _read_card(connection, card_id)


def _row_id(cursor: sqlite3.Cursor) -> int:
    if cursor.lastrowid is None:
        raise NotFoundError("The row was not stored.")
    return cursor.lastrowid


def _clamp(position: int, size: int) -> int:
    return max(0, min(position, size))


def _require(connection: sqlite3.Connection, query: str, row_id: int) -> None:
    if connection.execute(query, (row_id,)).fetchone() is None:
        raise NotFoundError(f"No such row: {row_id}")


def _read_list(connection: sqlite3.Connection, list_id: int) -> CardList:
    row = connection.execute(
        "SELECT id, board_id, name, position FROM lists WHERE id = ?", (list_id,)
    ).fetchone()
    if row is None:
        raise NotFoundError(f"No such list: {list_id}")
    return CardList(*row)


def _read_card(connection: sqlite3.Connection, card_id: int) -> Card:
    row = connection.execute(_CARD_BY_ID_SQL, (card_id,)).fetchone()
    if row is None:
        raise NotFoundError(f"No such card: {card_id}")
    return _card_from_row(row)


def _card_from_row(row: tuple[Any, ...]) -> Card:
    return Card(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], bool(row[7]), row[8]
    )


def _migrate(connection: sqlite3.Connection) -> None:
    """Bring a database file written by an older version up to the current schema."""
    version = connection.execute("PRAGMA user_version").fetchone()[0]
    if version >= constants.SCHEMA_VERSION:
        return
    existing = {row[1] for row in connection.execute("PRAGMA table_info(cards)")}
    for column, statement in _ADD_CARD_DETAIL_COLUMNS:
        if column not in existing:
            connection.execute(statement)
    connection.execute(_SET_SCHEMA_VERSION_SQL)


def _list_ids(connection: sqlite3.Connection, board_id: int) -> list[int]:
    rows = connection.execute(
        "SELECT id FROM lists WHERE board_id = ? ORDER BY position", (board_id,)
    ).fetchall()
    return [row[0] for row in rows]


def _card_ids(connection: sqlite3.Connection, list_id: int) -> list[int]:
    rows = connection.execute(
        "SELECT id FROM cards WHERE list_id = ? ORDER BY position", (list_id,)
    ).fetchall()
    return [row[0] for row in rows]


def _renumber_lists(
    connection: sqlite3.Connection, board_id: int, ids: list[int]
) -> None:
    for position, list_id in enumerate(ids):
        connection.execute(
            "UPDATE lists SET position = ? WHERE id = ? AND board_id = ?",
            (position, list_id, board_id),
        )


def _renumber_cards(
    connection: sqlite3.Connection, list_id: int, ids: list[int]
) -> None:
    for position, card_id in enumerate(ids):
        connection.execute(
            "UPDATE cards SET position = ?, list_id = ? WHERE id = ?",
            (position, list_id, card_id),
        )
