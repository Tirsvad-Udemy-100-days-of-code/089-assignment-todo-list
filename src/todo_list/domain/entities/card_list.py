"""@brief The list entity; named CardList because list is a Python builtin."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CardList:
    """@brief A list holds cards and sits at a position on its board.

    @param id The identifier given by the store.
    @param board_id The board it belongs to.
    @param name The list name, for example Backlog.
    @param position The zero-based place from left to right.
    """

    id: int
    board_id: int
    name: str
    position: int
