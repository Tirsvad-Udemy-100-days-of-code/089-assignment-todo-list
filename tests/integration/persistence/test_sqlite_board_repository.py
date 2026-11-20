"""Integration tests of the SQLite repository on a temporary file."""

from pathlib import Path

import pytest

from todo_list.domain.errors.board_errors import NotFoundError
from todo_list.infrastructure.persistence.sqlite_board_repository import (
    SqliteBoardRepository,
)


@pytest.fixture
def repository(tmp_path: Path) -> SqliteBoardRepository:
    return SqliteBoardRepository(tmp_path / "test.sqlite3")


def _titles(repository: SqliteBoardRepository, list_id: int) -> list[str]:
    return [card.title for card in repository.cards_of(list_id)]


def test_first_board_is_none_on_an_empty_store(
    repository: SqliteBoardRepository,
) -> None:
    assert repository.first_board() is None


def test_data_survives_a_new_repository_on_the_same_file(tmp_path: Path) -> None:
    path = tmp_path / "keep.sqlite3"
    board = SqliteBoardRepository(path).add_board("Board")

    assert SqliteBoardRepository(path).first_board() == board


def test_lists_are_returned_left_to_right(repository: SqliteBoardRepository) -> None:
    board = repository.add_board("Board")
    repository.add_list(board.id, "A")
    repository.add_list(board.id, "B")

    assert [item.name for item in repository.lists_of(board.id)] == ["A", "B"]


def test_rename_list_and_unknown_list(repository: SqliteBoardRepository) -> None:
    board = repository.add_board("Board")
    created = repository.add_list(board.id, "A")

    assert repository.rename_list(created.id, "Z").name == "Z"
    with pytest.raises(NotFoundError):
        repository.rename_list(99, "Z")


def test_add_list_to_an_unknown_board_fails(repository: SqliteBoardRepository) -> None:
    with pytest.raises(NotFoundError):
        repository.add_list(99, "A")


def test_move_list_renumbers_without_gaps(repository: SqliteBoardRepository) -> None:
    board = repository.add_board("Board")
    first = repository.add_list(board.id, "A")
    repository.add_list(board.id, "B")
    repository.add_list(board.id, "C")

    repository.move_list(first.id, 1)

    lists = repository.lists_of(board.id)
    assert [(item.name, item.position) for item in lists] == [
        ("B", 0),
        ("A", 1),
        ("C", 2),
    ]


def test_delete_list_removes_its_cards_and_closes_the_gap(
    repository: SqliteBoardRepository,
) -> None:
    board = repository.add_board("Board")
    first = repository.add_list(board.id, "A")
    repository.add_list(board.id, "B")
    repository.add_card(first.id, "One")

    repository.delete_list(first.id)

    assert repository.cards_of(first.id) == []
    assert [(item.name, item.position) for item in repository.lists_of(board.id)] == [
        ("B", 0)
    ]
    with pytest.raises(NotFoundError):
        repository.delete_list(first.id)


def test_cards_are_added_at_the_bottom_and_renamed(
    repository: SqliteBoardRepository,
) -> None:
    board = repository.add_board("Board")
    card_list = repository.add_list(board.id, "A")
    repository.add_card(card_list.id, "One")
    two = repository.add_card(card_list.id, "Two")

    assert repository.rename_card(two.id, "Deux").title == "Deux"
    assert _titles(repository, card_list.id) == ["One", "Deux"]
    with pytest.raises(NotFoundError):
        repository.rename_card(99, "x")
    with pytest.raises(NotFoundError):
        repository.add_card(99, "x")


def test_delete_card_closes_the_gap(repository: SqliteBoardRepository) -> None:
    board = repository.add_board("Board")
    card_list = repository.add_list(board.id, "A")
    one = repository.add_card(card_list.id, "One")
    repository.add_card(card_list.id, "Two")

    repository.delete_card(one.id)

    assert [(c.title, c.position) for c in repository.cards_of(card_list.id)] == [
        ("Two", 0)
    ]
    with pytest.raises(NotFoundError):
        repository.delete_card(one.id)


def test_move_card_within_a_list(repository: SqliteBoardRepository) -> None:
    board = repository.add_board("Board")
    card_list = repository.add_list(board.id, "A")
    one = repository.add_card(card_list.id, "One")
    repository.add_card(card_list.id, "Two")
    repository.add_card(card_list.id, "Three")

    repository.move_card(one.id, card_list.id, 2)

    assert _titles(repository, card_list.id) == ["Two", "Three", "One"]


def test_move_card_to_another_list_renumbers_both(
    repository: SqliteBoardRepository,
) -> None:
    board = repository.add_board("Board")
    source = repository.add_list(board.id, "A")
    target = repository.add_list(board.id, "B")
    one = repository.add_card(source.id, "One")
    repository.add_card(source.id, "Two")
    repository.add_card(target.id, "Three")

    moved = repository.move_card(one.id, target.id, 0)

    assert moved.list_id == target.id
    assert _titles(repository, target.id) == ["One", "Three"]
    assert [(c.title, c.position) for c in repository.cards_of(source.id)] == [
        ("Two", 0)
    ]
    with pytest.raises(NotFoundError):
        repository.move_card(one.id, 99, 0)
