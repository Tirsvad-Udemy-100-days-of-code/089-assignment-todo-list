"""@brief An in-memory board repository for unit tests of the use cases."""

from dataclasses import replace

from todo_list.domain.entities.board import Board
from todo_list.domain.entities.card import Card
from todo_list.domain.entities.card_list import CardList
from todo_list.domain.entities.comment import Comment
from todo_list.domain.errors.board_errors import NotFoundError


class InMemoryBoardRepository:
    """@brief Keeps boards, lists and cards in dictionaries."""

    def __init__(self) -> None:
        """@brief Start empty."""
        self._boards: dict[int, Board] = {}
        self._lists: dict[int, CardList] = {}
        self._cards: dict[int, Card] = {}
        self._comments: dict[int, Comment] = {}
        self._next_id = 1

    def _new_id(self) -> int:
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def first_board(self) -> Board | None:
        """@brief Return the first board or None."""
        return next(iter(self._boards.values()), None)

    def add_board(self, name: str) -> Board:
        """@brief Store a board."""
        board = Board(self._new_id(), name)
        self._boards[board.id] = board
        return board

    def lists_of(self, board_id: int) -> list[CardList]:
        """@brief Return the lists of a board in order."""
        lists = [item for item in self._lists.values() if item.board_id == board_id]
        return sorted(lists, key=lambda item: item.position)

    def cards_of(self, list_id: int) -> list[Card]:
        """@brief Return the cards of a list in order."""
        cards = [
            self._counted(item)
            for item in self._cards.values()
            if item.list_id == list_id
        ]
        return sorted(cards, key=lambda item: item.position)

    def _counted(self, card: Card) -> Card:
        count = sum(1 for item in self._comments.values() if item.card_id == card.id)
        return replace(card, comment_count=count)

    def get_card(self, card_id: int) -> Card:
        """@brief Return one card."""
        return self._counted(self._get_card(card_id))

    def update_card_details(
        self,
        card_id: int,
        label: str,
        description: str,
        due_date: str | None,
        done: bool,
    ) -> Card:
        """@brief Replace the details of a card."""
        card = replace(
            self._get_card(card_id),
            label=label,
            description=description,
            due_date=due_date,
            done=done,
        )
        self._cards[card_id] = card
        return self._counted(card)

    def add_comment(self, card_id: int, text: str, created_at: str) -> Comment:
        """@brief Add a comment."""
        self._get_card(card_id)
        comment = Comment(self._new_id(), card_id, text, created_at)
        self._comments[comment.id] = comment
        return comment

    def comments_of(self, card_id: int) -> list[Comment]:
        """@brief Return the comments of a card, oldest first."""
        self._get_card(card_id)
        found = [item for item in self._comments.values() if item.card_id == card_id]
        return sorted(found, key=lambda item: item.id)

    def delete_comment(self, comment_id: int) -> None:
        """@brief Delete a comment."""
        if comment_id not in self._comments:
            raise NotFoundError(str(comment_id))
        del self._comments[comment_id]

    def add_list(self, board_id: int, name: str) -> CardList:
        """@brief Add a list at the end."""
        if board_id not in self._boards:
            raise NotFoundError(str(board_id))
        item = CardList(self._new_id(), board_id, name, len(self.lists_of(board_id)))
        self._lists[item.id] = item
        return item

    def rename_list(self, list_id: int, name: str) -> CardList:
        """@brief Rename a list."""
        item = replace(self._get_list(list_id), name=name)
        self._lists[list_id] = item
        return item

    def delete_list(self, list_id: int) -> None:
        """@brief Delete a list and its cards."""
        board_id = self._get_list(list_id).board_id
        for card in self.cards_of(list_id):
            self._drop_comments(card.id)
            del self._cards[card.id]
        del self._lists[list_id]
        for position, item in enumerate(self.lists_of(board_id)):
            self._lists[item.id] = replace(item, position=position)

    def move_list(self, list_id: int, position: int) -> CardList:
        """@brief Move a list."""
        board_id = self._get_list(list_id).board_id
        ordered = [item for item in self.lists_of(board_id) if item.id != list_id]
        ordered.insert(max(0, min(position, len(ordered))), self._lists[list_id])
        for index, item in enumerate(ordered):
            self._lists[item.id] = replace(item, position=index)
        return self._lists[list_id]

    def add_card(self, list_id: int, title: str) -> Card:
        """@brief Add a card at the bottom."""
        self._get_list(list_id)
        card = Card(self._new_id(), list_id, title, len(self.cards_of(list_id)))
        self._cards[card.id] = card
        return card

    def rename_card(self, card_id: int, title: str) -> Card:
        """@brief Rename a card."""
        card = replace(self._get_card(card_id), title=title)
        self._cards[card_id] = card
        return self._counted(card)

    def delete_card(self, card_id: int) -> None:
        """@brief Delete a card."""
        list_id = self._get_card(card_id).list_id
        self._drop_comments(card_id)
        del self._cards[card_id]
        for position, card in enumerate(self.cards_of(list_id)):
            self._cards[card.id] = replace(card, position=position)

    def move_card(self, card_id: int, list_id: int, position: int) -> Card:
        """@brief Move a card."""
        source_id = self._get_card(card_id).list_id
        self._get_list(list_id)
        ordered = [card for card in self.cards_of(list_id) if card.id != card_id]
        ordered.insert(max(0, min(position, len(ordered))), self._cards[card_id])
        for index, card in enumerate(ordered):
            self._cards[card.id] = replace(card, list_id=list_id, position=index)
        for index, card in enumerate(self.cards_of(source_id)):
            self._cards[card.id] = replace(card, position=index)
        return self._counted(self._cards[card_id])

    def _drop_comments(self, card_id: int) -> None:
        for comment in self.comments_of(card_id):
            del self._comments[comment.id]

    def _get_list(self, list_id: int) -> CardList:
        if list_id not in self._lists:
            raise NotFoundError(str(list_id))
        return self._lists[list_id]

    def _get_card(self, card_id: int) -> Card:
        if card_id not in self._cards:
            raise NotFoundError(str(card_id))
        return self._cards[card_id]
