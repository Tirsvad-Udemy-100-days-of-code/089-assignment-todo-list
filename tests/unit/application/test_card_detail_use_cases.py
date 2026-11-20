"""Unit tests of the card detail and comment use cases."""

import pytest

from support.in_memory_board_repository import InMemoryBoardRepository
from todo_list.application.use_cases.board_use_cases import GetBoard
from todo_list.application.use_cases.card_use_cases import (
    AddComment,
    CreateCard,
    DeleteCard,
    DeleteComment,
    GetCard,
    UpdateCardDetails,
)
from todo_list.domain.errors.board_errors import (
    InvalidDetailError,
    InvalidNameError,
    NotFoundError,
)


@pytest.fixture
def repository() -> InMemoryBoardRepository:
    repository = InMemoryBoardRepository()
    board = repository.add_board("Board")
    repository.add_list(board.id, "A")
    return repository


def _card_id(repository: InMemoryBoardRepository) -> int:
    return CreateCard(repository).execute(2, "One").id


def test_update_changes_only_the_given_fields(
    repository: InMemoryBoardRepository,
) -> None:
    card_id = _card_id(repository)
    UpdateCardDetails(repository).execute(
        card_id, label="Red", description="d", due_date="2030-01-02", done=True
    )

    card = UpdateCardDetails(repository).execute(card_id, title=" Uno ")

    assert (card.title, card.label, card.description) == ("Uno", "red", "d")
    assert (card.due_date, card.done) == ("2030-01-02", True)


def test_update_clears_the_due_date_with_none(
    repository: InMemoryBoardRepository,
) -> None:
    card_id = _card_id(repository)
    UpdateCardDetails(repository).execute(card_id, due_date="2030-01-02")

    card = UpdateCardDetails(repository).execute(card_id, due_date=None, label="")

    assert card.due_date is None


@pytest.mark.parametrize(
    ("field", "value"),
    [("label", "pink"), ("due_date", "nope"), ("description", "x" * 2001)],
)
def test_update_rejects_invalid_details(
    repository: InMemoryBoardRepository, field: str, value: str
) -> None:
    card_id = _card_id(repository)
    with pytest.raises(InvalidDetailError):
        UpdateCardDetails(repository).execute(card_id, **{field: value})  # type: ignore[arg-type]


def test_update_rejects_an_empty_title_and_an_unknown_card(
    repository: InMemoryBoardRepository,
) -> None:
    card_id = _card_id(repository)
    with pytest.raises(InvalidNameError):
        UpdateCardDetails(repository).execute(card_id, title=" ")
    with pytest.raises(NotFoundError):
        UpdateCardDetails(repository).execute(99, done=True)


def test_comments_are_added_listed_and_counted(
    repository: InMemoryBoardRepository,
) -> None:
    card_id = _card_id(repository)
    first = AddComment(repository).execute(card_id, " First ")
    AddComment(repository).execute(card_id, "Second")

    details = GetCard(repository).execute(card_id)

    assert [c.text for c in details.comments] == ["First", "Second"]
    assert details.comment_count == 2
    assert first.created_at.endswith("+00:00")
    assert GetBoard(repository).execute().lists[0].cards[0].comment_count == 2


def test_delete_comment_removes_it(repository: InMemoryBoardRepository) -> None:
    card_id = _card_id(repository)
    comment = AddComment(repository).execute(card_id, "x")

    DeleteComment(repository).execute(comment.id)

    assert GetCard(repository).execute(card_id).comments == ()
    with pytest.raises(NotFoundError):
        DeleteComment(repository).execute(comment.id)


def test_add_comment_rejects_empty_text_and_unknown_card(
    repository: InMemoryBoardRepository,
) -> None:
    with pytest.raises(InvalidDetailError):
        AddComment(repository).execute(_card_id(repository), " ")
    with pytest.raises(NotFoundError):
        AddComment(repository).execute(99, "x")
    with pytest.raises(NotFoundError):
        GetCard(repository).execute(99)


def test_deleting_a_card_deletes_its_comments(
    repository: InMemoryBoardRepository,
) -> None:
    card_id = _card_id(repository)
    comment = AddComment(repository).execute(card_id, "x")

    DeleteCard(repository).execute(card_id)

    with pytest.raises(NotFoundError):
        DeleteComment(repository).execute(comment.id)
