"""@brief Data the presentation layer shows."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CardDto:
    """@brief A card as shown on the board."""

    id: int
    title: str


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
