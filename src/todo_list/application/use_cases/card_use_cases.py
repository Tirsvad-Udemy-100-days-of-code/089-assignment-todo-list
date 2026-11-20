"""@brief Use cases about cards."""

from todo_list.domain.entities.card import Card
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
