"""Unit tests of the list use cases."""

import pytest

from support.in_memory_board_repository import InMemoryBoardRepository
from todo_list.application.use_cases.list_use_cases import (
    CreateList,
    DeleteList,
    MoveList,
    RenameList,
)
from todo_list.domain.errors.board_errors import InvalidNameError, NotFoundError


@pytest.fixture
def repository() -> InMemoryBoardRepository:
    repository = InMemoryBoardRepository()
    repository.add_board("Board")
    return repository


def test_create_list_trims_the_name_and_appends(
    repository: InMemoryBoardRepository,
) -> None:
    CreateList(repository).execute(1, "A")
    created = CreateList(repository).execute(1, "  B ")

    assert (created.name, created.position) == ("B", 1)


def test_create_list_rejects_an_empty_name(repository: InMemoryBoardRepository) -> None:
    with pytest.raises(InvalidNameError):
        CreateList(repository).execute(1, " ")


def test_rename_list_changes_the_name(repository: InMemoryBoardRepository) -> None:
    created = CreateList(repository).execute(1, "A")

    assert RenameList(repository).execute(created.id, "Z").name == "Z"


def test_rename_list_rejects_an_unknown_list(
    repository: InMemoryBoardRepository,
) -> None:
    with pytest.raises(NotFoundError):
        RenameList(repository).execute(99, "Z")


def test_delete_list_closes_the_gap(repository: InMemoryBoardRepository) -> None:
    first = CreateList(repository).execute(1, "A")
    CreateList(repository).execute(1, "B")

    DeleteList(repository).execute(first.id)

    assert [(item.name, item.position) for item in repository.lists_of(1)] == [("B", 0)]


def test_move_list_places_it_and_clamps_the_position(
    repository: InMemoryBoardRepository,
) -> None:
    first = CreateList(repository).execute(1, "A")
    CreateList(repository).execute(1, "B")
    CreateList(repository).execute(1, "C")

    MoveList(repository).execute(first.id, 99)

    assert [item.name for item in repository.lists_of(1)] == ["B", "C", "A"]
