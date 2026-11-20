"""@brief The one rule for names and titles."""

from todo_list import constants
from todo_list.domain.errors.board_errors import InvalidNameError


def clean_name(raw: str) -> str:
    """@brief Trim a name and check it.

    @param raw The text the user typed.
    @return The trimmed name.
    @throws InvalidNameError When the name is empty or longer than the limit.
    """
    name = raw.strip()
    if not name:
        raise InvalidNameError(constants.ERROR_NAME_EMPTY)
    if len(name) > constants.MAX_NAME_LENGTH:
        raise InvalidNameError(constants.ERROR_NAME_TOO_LONG)
    return name
