"""@brief Data the presentation layer shows."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CardDto:
    """@brief A card as shown on the board."""

    id: int
    title: str
    label: str = ""
    description: str = ""
    due_date: str | None = None
    done: bool = False
    comment_count: int = 0


@dataclass(frozen=True)
class CommentDto:
    """@brief A comment as shown on a card."""

    id: int
    card_id: int
    text: str
    created_at: str


@dataclass(frozen=True)
class CardDetailsDto:
    """@brief A card with its comments."""

    id: int
    list_id: int
    title: str
    label: str
    description: str
    due_date: str | None
    done: bool
    comment_count: int
    comments: tuple[CommentDto, ...]


@dataclass(frozen=True)
class ListDto:
    """@brief A list with its cards as shown on the board."""

    id: int
    name: str
    cards: tuple[CardDto, ...]


@dataclass(frozen=True)
class BoardDto:
    """@brief A board with its lists as shown on the page."""

    id: int
    name: str
    lists: tuple[ListDto, ...]
