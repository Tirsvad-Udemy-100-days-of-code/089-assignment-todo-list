"""Unit tests of the board use cases."""

from support.in_memory_board_repository import InMemoryBoardRepository
from todo_list import constants
from todo_list.application.use_cases.board_use_cases import EnsureDefaultBoard, GetBoard
from todo_list.application.use_cases.card_use_cases import CreateCard


def test_ensure_default_board_creates_the_five_lists_once() -> None:
    repository = InMemoryBoardRepository()

    first = EnsureDefaultBoard(repository).execute()
    second = EnsureDefaultBoard(repository).execute()

    assert first == second
    names = [item.name for item in repository.lists_of(first.id)]
    assert names == list(constants.DEFAULT_LIST_NAMES)


def test_get_board_returns_lists_in_order_with_their_cards() -> None:
    repository = InMemoryBoardRepository()
    board = EnsureDefaultBoard(repository).execute()
    backlog = repository.lists_of(board.id)[0]
    CreateCard(repository).execute(backlog.id, "Write tests")

    dto = GetBoard(repository).execute()

    assert [item.name for item in dto.lists][0] == "Backlog"
    assert [card.title for card in dto.lists[0].cards] == ["Write tests"]
    assert dto.lists[1].cards == ()
