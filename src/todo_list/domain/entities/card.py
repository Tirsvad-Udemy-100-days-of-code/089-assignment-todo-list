"""@brief The card entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """@brief A card is one task in a list.

    @param id The identifier given by the store.
    @param list_id The list it is in.
    @param title The task title.
    @param position The zero-based place from top to bottom.
    @param label The label colour, or empty for none.
    @param description The free text about the task.
    @param due_date The due date as YYYY-MM-DD, or None.
    @param done Whether the task is finished.
    @param comment_count How many comments the card has.
    """

    id: int
    list_id: int
    title: str
    position: int
    label: str = ""
    description: str = ""
    due_date: str | None = None
    done: bool = False
    comment_count: int = 0
