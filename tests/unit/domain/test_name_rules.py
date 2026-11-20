"""Unit tests of the name rule."""

import pytest

from todo_list import constants
from todo_list.domain.errors.board_errors import InvalidNameError
from todo_list.domain.name_rules import clean_name


def test_clean_name_trims_spaces() -> None:
    assert clean_name("  Backlog ") == "Backlog"


@pytest.mark.parametrize("raw", ["", "   ", "\t\n"])
def test_clean_name_rejects_empty_text(raw: str) -> None:
    with pytest.raises(InvalidNameError):
        clean_name(raw)


def test_clean_name_rejects_too_long_text() -> None:
    with pytest.raises(InvalidNameError):
        clean_name("x" * (constants.MAX_NAME_LENGTH + 1))


def test_clean_name_accepts_the_longest_name() -> None:
    assert len(clean_name("x" * constants.MAX_NAME_LENGTH)) == constants.MAX_NAME_LENGTH
