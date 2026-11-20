"""Unit tests of the card use cases."""

import pytest

from support.in_memory_board_repository import InMemoryBoardRepository
from todo_list.application.use_cases.card_use_cases import (
    CreateCard,
    DeleteCard,
    MoveCard,
    RenameCard,
)
from todo_list.domain.errors.board_errors import InvalidNameError, NotFoundError


@pytest.fixture
def repository() -> InMemoryBoardRepository:
    repository = InMemoryBoardRepository()
    board = repository.add_board("Board")
    repository.add_list(board.id, "A")
    repository.add_list(board.id, "B")
    return repository


def test_create_card_appends_to_the_list(repository: InMemoryBoardRepository) -> None:
    CreateCard(repository).execute(2, "One")
    second = CreateCard(repository).execute(2, " Two ")

    assert (second.title, second.position) == ("Two", 1)


def test_create_card_rejects_an_empty_title(
    repository: InMemoryBoardRepository,
) -> None:
    with pytest.raises(InvalidNameError):
        CreateCard(repository).execute(2, "")


def test_create_card_rejects_an_unknown_list(
    repository: InMemoryBoardRepository,
) -> None:
    with pytest.raises(NotFoundError):
        CreateCard(repository).execute(99, "One")


def test_rename_card_changes_the_title(repository: InMemoryBoardRepository) -> None:
    card = CreateCard(repository).execute(2, "One")

    assert RenameCard(repository).execute(card.id, "Uno").title == "Uno"


def test_delete_card_closes_the_gap(repository: InMemoryBoardRepository) -> None:
    first = CreateCard(repository).execute(2, "One")
    CreateCard(repository).execute(2, "Two")

    DeleteCard(repository).execute(first.id)

    assert [(c.title, c.position) for c in repository.cards_of(2)] == [("Two", 0)]


def test_move_card_to_another_list_renumbers_both_lists(
    repository: InMemoryBoardRepository,
) -> None:
    one = CreateCard(repository).execute(2, "One")
    CreateCard(repository).execute(2, "Two")
    CreateCard(repository).execute(3, "Three")

    MoveCard(repository).execute(one.id, 3, 0)

    assert [c.title for c in repository.cards_of(3)] == ["One", "Three"]
    assert [(c.title, c.position) for c in repository.cards_of(2)] == [("Two", 0)]
