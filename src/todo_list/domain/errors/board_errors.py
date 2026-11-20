"""@brief Errors of the board rules."""


class InvalidNameError(ValueError):
    """@brief A name or title is empty or too long."""


class NotFoundError(LookupError):
    """@brief A board, list or card does not exist."""


class InvalidDetailError(ValueError):
    """@brief A label, description, due date or comment is not valid."""
