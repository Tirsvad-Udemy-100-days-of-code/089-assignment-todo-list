"""@brief Use cases about the board itself."""

from todo_list import constants
from todo_list.application.dto.board_dto import BoardDto, CardDto, ListDto
from todo_list.domain.entities.board import Board
from todo_list.domain.repositories.board_repository import BoardRepository


class EnsureDefaultBoard:
    """@brief Make sure a board with the default lists exists."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self) -> Board:
        """@brief Return the first board; create it with the default lists if none."""
        board = self._repository.first_board()
        if board is not None:
            return board
        board = self._repository.add_board(constants.DEFAULT_BOARD_NAME)
        for name in constants.DEFAULT_LIST_NAMES:
            self._repository.add_list(board.id, name)
        return board


class GetBoard:
    """@brief Read the whole board for display."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self) -> BoardDto:
        """@brief Return the first board with its lists and cards."""
        board = EnsureDefaultBoard(self._repository).execute()
        lists = tuple(
            ListDto(
                card_list.id,
                card_list.name,
                tuple(
                    CardDto(card.id, card.title)
                    for card in self._repository.cards_of(card_list.id)
                ),
            )
            for card_list in self._repository.lists_of(board.id)
        )
        return BoardDto(board.id, board.name, lists)
