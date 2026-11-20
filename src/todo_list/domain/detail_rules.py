"""@brief The rules for the details of a card: label, description, due date, comment."""

from datetime import date

from todo_list import constants
from todo_list.domain.errors.board_errors import InvalidDetailError


def clean_label(raw: str) -> str:
    """@brief Check a label colour.

    @param raw A colour of the palette, or empty for none.
    @return The colour in lower case.
    @throws InvalidDetailError When the colour is not in the palette.
    """
    label = raw.strip().lower()
    if label and label not in constants.LABEL_COLOURS:
        raise InvalidDetailError(constants.ERROR_LABEL_INVALID)
    return label


def clean_description(raw: str) -> str:
    """@brief Trim a description and check its length.

    @throws InvalidDetailError When it is longer than the limit.
    """
    description = raw.strip()
    if len(description) > constants.MAX_DESCRIPTION_LENGTH:
        raise InvalidDetailError(constants.ERROR_DESCRIPTION_TOO_LONG)
    return description


def clean_due_date(raw: str | None) -> str | None:
    """@brief Check a due date.

    @param raw A date as YYYY-MM-DD, or None for no due date.
    @return The date in ISO form, or None.
    @throws InvalidDetailError When the text is not a calendar date.
    """
    if raw is None:
        return None
    text = raw.strip()
    try:
        parsed = date.fromisoformat(text)
    except ValueError as error:
        raise InvalidDetailError(constants.ERROR_DUE_DATE_INVALID) from error
    if parsed.isoformat() != text:
        raise InvalidDetailError(constants.ERROR_DUE_DATE_INVALID)
    return text


def clean_comment(raw: str) -> str:
    """@brief Trim a comment and check it.

    @throws InvalidDetailError When it is empty or longer than the limit.
    """
    text = raw.strip()
    if not text:
        raise InvalidDetailError(constants.ERROR_COMMENT_EMPTY)
    if len(text) > constants.MAX_COMMENT_LENGTH:
        raise InvalidDetailError(constants.ERROR_COMMENT_TOO_LONG)
    return text
