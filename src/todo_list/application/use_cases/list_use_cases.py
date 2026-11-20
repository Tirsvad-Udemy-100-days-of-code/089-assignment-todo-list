"""@brief Use cases about lists."""

from todo_list.domain.entities.card_list import CardList
from todo_list.domain.name_rules import clean_name
from todo_list.domain.repositories.board_repository import BoardRepository


class CreateList:
    """@brief Add a list to a board."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, board_id: int, name: str) -> CardList:
        """@brief Add a list at the right end.

        @throws InvalidNameError When the name is not valid.
        """
        return self._repository.add_list(board_id, clean_name(name))


class RenameList:
    """@brief Rename a list."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, list_id: int, name: str) -> CardList:
        """@brief Change the name of a list.

        @throws InvalidNameError When the name is not valid.
        @throws NotFoundError When the list does not exist.
        """
        return self._repository.rename_list(list_id, clean_name(name))


class DeleteList:
    """@brief Delete a list and its cards."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, list_id: int) -> None:
        """@brief Delete the list.

        @throws NotFoundError When the list does not exist.
        """
        self._repository.delete_list(list_id)


class MoveList:
    """@brief Move a list to another place on its board."""

    def __init__(self, repository: BoardRepository) -> None:
        """@param repository The store."""
        self._repository = repository

    def execute(self, list_id: int, position: int) -> CardList:
        """@brief Move the list; a position past the end means the end.

        @throws NotFoundError When the list does not exist.
        """
        return self._repository.move_list(list_id, position)
