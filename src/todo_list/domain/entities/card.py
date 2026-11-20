"""@brief The card entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """@brief A card is one task in a list.

    @param id The identifier given by the store.
    @param list_id The list it is in.
    @param title The task title.
    @param position The zero-based place from top to bottom.
    """

    id: int
    list_id: int
    title: str
    position: int
