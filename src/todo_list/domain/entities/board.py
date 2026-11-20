"""@brief The board entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Board:
    """@brief A board holds lists.

    @param id The identifier given by the store.
    @param name The board name.
    """

    id: int
    name: str
