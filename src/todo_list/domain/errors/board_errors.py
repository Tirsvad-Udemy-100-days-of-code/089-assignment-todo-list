"""@brief Errors of the board rules."""


class InvalidNameError(ValueError):
    """@brief A name or title is empty or too long."""


class NotFoundError(LookupError):
    """@brief A board, list or card does not exist."""
