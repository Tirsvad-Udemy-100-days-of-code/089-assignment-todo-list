"""@brief The port the application uses to store boards, lists and cards."""

from typing import Protocol

from todo_list.domain.entities.board import Board
from todo_list.domain.entities.card import Card
from todo_list.domain.entities.card_list import CardList


class BoardRepository(Protocol):
    """@brief Storage of boards, lists and cards.

    Positions are zero-based and without gaps; the store keeps them so.
    A missing id raises NotFoundError.
    """

    def first_board(self) -> Board | None:
        """@brief Return the first board, or None when there is none."""
        ...

    def add_board(self, name: str) -> Board:
        """@brief Store a new board."""
        ...

    def lists_of(self, board_id: int) -> list[CardList]:
        """@brief Return the lists of a board, left to right."""
        ...

    def cards_of(self, list_id: int) -> list[Card]:
        """@brief Return the cards of a list, top to bottom."""
        ...

    def add_list(self, board_id: int, name: str) -> CardList:
        """@brief Add a list at the right end of a board."""
        ...

    def rename_list(self, list_id: int, name: str) -> CardList:
        """@brief Change the name of a list."""
        ...

    def delete_list(self, list_id: int) -> None:
        """@brief Delete a list and its cards."""
        ...

    def move_list(self, list_id: int, position: int) -> CardList:
        """@brief Move a list to a position on its board."""
        ...

    def add_card(self, list_id: int, title: str) -> Card:
        """@brief Add a card at the bottom of a list."""
        ...

    def rename_card(self, card_id: int, title: str) -> Card:
        """@brief Change the title of a card."""
        ...

    def delete_card(self, card_id: int) -> None:
        """@brief Delete a card."""
        ...

    def move_card(self, card_id: int, list_id: int, position: int) -> Card:
        """@brief Move a card to a position in a list, possibly another list."""
        ...
