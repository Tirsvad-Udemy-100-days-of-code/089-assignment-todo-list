"""@brief Use cases about cards."""

from datetime import UTC, datetime
from enum import Enum

from todo_list.application.dto.board_dto import CardDetailsDto, CommentDto
from todo_list.domain.detail_rules import (
    clean_comment,
    clean_description,
    clean_due_date,
    clean_label,
)
from todo_list.domain.entities.card import Card
from todo_list.domain.entities.comment import Comment
from todo_list.domain.name_rules import clean_name
from todo_list.domain.repositories.board_repository import BoardRepository


class CreateCard:
    """@brief Add a card to a list."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, list_id: int, title: str) -> Card:
        """@brief Add a card at the bottom of the list.

        @throws InvalidNameError When the title is not valid.
        @throws NotFoundError When the list does not exist.
        """
        return self._repository.add_card(list_id, clean_name(title))


class RenameCard:
    """@brief Change the title of a card."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, card_id: int, title: str) -> Card:
        """@brief Change the title.

        @throws InvalidNameError When the title is not valid.
        @throws NotFoundError When the card does not exist.
        """
        return self._repository.rename_card(card_id, clean_name(title))


class DeleteCard:
    """@brief Delete a card."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, card_id: int) -> None:
        """@brief Delete the card.

        @throws NotFoundError When the card does not exist.
        """
        self._repository.delete_card(card_id)


class MoveCard:
    """@brief Move a card within its list or to another list."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, card_id: int, list_id: int, position: int) -> Card:
        """@brief Move the card; a position past the end means the bottom.

        @throws NotFoundError When the card or the list does not exist.
        """
        return self._repository.move_card(card_id, list_id, position)


class _Unset(Enum):
    """@brief Marks a field the caller did not give."""

    UNSET = "unset"


## @brief Value of a field that was not given, so it stays unchanged.
UNSET = _Unset.UNSET


class UpdateCardDetails:
    """@brief Change the given fields of a card; the others stay as they are."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(
        self,
        card_id: int,
        title: str | None = None,
        label: str | None = None,
        description: str | None = None,
        due_date: str | None | _Unset = UNSET,
        done: bool | None = None,
    ) -> Card:
        """@brief Change the card.

        @param card_id The card.
        @param title New title, or None to keep it.
        @param label New label colour, or None to keep it; empty clears it.
        @param description New description, or None to keep it.
        @param due_date New date, None to clear it, or UNSET to keep it.
        @param done New done state, or None to keep it.
        @throws InvalidNameError When the title is not valid.
        @throws InvalidDetailError When a detail is not valid.
        @throws NotFoundError When the card does not exist.
        """
        card = self._repository.get_card(card_id)
        new_label = card.label if label is None else clean_label(label)
        new_description = (
            card.description if description is None else clean_description(description)
        )
        new_due = (
            card.due_date if isinstance(due_date, _Unset) else clean_due_date(due_date)
        )
        new_title = card.title if title is None else clean_name(title)
        new_done = card.done if done is None else done
        if new_title != card.title:
            self._repository.rename_card(card_id, new_title)
        return self._repository.update_card_details(
            card_id, new_label, new_description, new_due, new_done
        )


class GetCard:
    """@brief Read a card with its comments."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, card_id: int) -> CardDetailsDto:
        """@brief Return the card details.

        @throws NotFoundError When the card does not exist.
        """
        card = self._repository.get_card(card_id)
        comments = tuple(
            _comment_dto(comment) for comment in self._repository.comments_of(card_id)
        )
        return CardDetailsDto(
            card.id,
            card.list_id,
            card.title,
            card.label,
            card.description,
            card.due_date,
            card.done,
            card.comment_count,
            comments,
        )


class AddComment:
    """@brief Add a comment to a card."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, card_id: int, text: str) -> CommentDto:
        """@brief Add the comment, stamped with the current UTC time.

        @throws InvalidDetailError When the text is empty or too long.
        @throws NotFoundError When the card does not exist.
        """
        created_at = datetime.now(UTC).isoformat()
        comment = self._repository.add_comment(card_id, clean_comment(text), created_at)
        return _comment_dto(comment)


class DeleteComment:
    """@brief Delete a comment."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, comment_id: int) -> None:
        """@brief Delete the comment.

        @throws NotFoundError When the comment does not exist.
        """
        self._repository.delete_comment(comment_id)


def _comment_dto(comment: Comment) -> CommentDto:
    return CommentDto(comment.id, comment.card_id, comment.text, comment.created_at)
