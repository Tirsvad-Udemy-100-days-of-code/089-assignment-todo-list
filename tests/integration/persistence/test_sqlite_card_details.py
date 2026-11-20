"""Integration tests of card details, comments and the schema migration."""

import sqlite3
from pathlib import Path

import pytest

from todo_list.domain.errors.board_errors import NotFoundError
from todo_list.infrastructure.persistence.sqlite_board_repository import (
    SqliteBoardRepository,
)

_OLD_SCHEMA = """
CREATE TABLE boards (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);
CREATE TABLE lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_id INTEGER NOT NULL REFERENCES boards(id) ON DELETE CASCADE,
    name TEXT NOT NULL, position INTEGER NOT NULL);
CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    list_id INTEGER NOT NULL REFERENCES lists(id) ON DELETE CASCADE,
    title TEXT NOT NULL, position INTEGER NOT NULL);
INSERT INTO boards (name) VALUES ('Old');
INSERT INTO lists (board_id, name, position) VALUES (1, 'A', 0);
INSERT INTO cards (list_id, title, position) VALUES (1, 'Kept', 0);
"""


@pytest.fixture
def repository(tmp_path: Path) -> SqliteBoardRepository:
    repository = SqliteBoardRepository(tmp_path / "details.sqlite3")
    board = repository.add_board("Board")
    repository.add_list(board.id, "A")
    return repository


def test_old_database_is_migrated_and_keeps_its_cards(tmp_path: Path) -> None:
    path = tmp_path / "old.sqlite3"
    with sqlite3.connect(path) as connection:
        connection.executescript(_OLD_SCHEMA)
    connection.close()

    repository = SqliteBoardRepository(path)
    card = repository.cards_of(1)[0]
    updated = repository.update_card_details(card.id, "red", "d", "2030-01-02", True)
    reopened = SqliteBoardRepository(path)

    assert (card.title, card.label, card.due_date, card.done) == (
        "Kept",
        "",
        None,
        False,
    )
    assert reopened.get_card(card.id) == updated
    assert reopened.add_comment(card.id, "x", "t").card_id == card.id


def test_update_card_details_roundtrips(repository: SqliteBoardRepository) -> None:
    card = repository.add_card(1, "One")

    updated = repository.update_card_details(
        card.id, "blue", "text", "2030-05-06", True
    )

    assert (updated.label, updated.description) == ("blue", "text")
    assert (updated.due_date, updated.done) == ("2030-05-06", True)
    assert repository.cards_of(1)[0] == updated


def test_comments_are_stored_counted_and_deleted(
    repository: SqliteBoardRepository,
) -> None:
    card = repository.add_card(1, "One")
    first = repository.add_comment(card.id, "a", "2030-01-01T00:00:00+00:00")
    repository.add_comment(card.id, "b", "2030-01-02T00:00:00+00:00")

    assert [c.text for c in repository.comments_of(card.id)] == ["a", "b"]
    assert repository.get_card(card.id).comment_count == 2

    repository.delete_comment(first.id)
    assert [c.text for c in repository.comments_of(card.id)] == ["b"]


def test_deleting_a_card_or_list_deletes_its_comments(
    repository: SqliteBoardRepository,
) -> None:
    card = repository.add_card(1, "One")
    other = repository.add_card(1, "Two")
    repository.add_comment(card.id, "a", "t")
    repository.add_comment(other.id, "b", "t")

    repository.delete_card(card.id)
    repository.delete_list(1)

    with sqlite3.connect(repository._path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM comments").fetchone()[0] == 0


def test_unknown_ids_raise_not_found(repository: SqliteBoardRepository) -> None:
    with pytest.raises(NotFoundError):
        repository.get_card(99)
    with pytest.raises(NotFoundError):
        repository.update_card_details(99, "", "", None, False)
    with pytest.raises(NotFoundError):
        repository.add_comment(99, "x", "t")
    with pytest.raises(NotFoundError):
        repository.comments_of(99)
    with pytest.raises(NotFoundError):
        repository.delete_comment(99)
