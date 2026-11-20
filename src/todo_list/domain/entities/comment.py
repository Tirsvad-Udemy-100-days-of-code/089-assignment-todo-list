"""@brief The comment entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Comment:
    """@brief A text note on a card.

    @param id The identifier given by the store.
    @param card_id The card it belongs to.
    @param text The comment text.
    @param created_at When it was written, as an ISO 8601 timestamp.
    """

    id: int
    card_id: int
    text: str
    created_at: str
