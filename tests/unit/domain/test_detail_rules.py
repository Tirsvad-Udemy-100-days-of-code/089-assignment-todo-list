"""Unit tests of the card detail rules."""

import pytest

from todo_list import constants
from todo_list.domain.detail_rules import (
    clean_comment,
    clean_description,
    clean_due_date,
    clean_label,
)
from todo_list.domain.errors.board_errors import InvalidDetailError


@pytest.mark.parametrize("colour", constants.LABEL_COLOURS)
def test_clean_label_accepts_every_colour_of_the_palette(colour: str) -> None:
    assert clean_label(colour) == colour


def test_clean_label_accepts_empty_and_normalises_case() -> None:
    assert clean_label("") == ""
    assert clean_label(" Red ") == "red"


def test_clean_label_rejects_a_colour_outside_the_palette() -> None:
    with pytest.raises(InvalidDetailError):
        clean_label("pink")


def test_clean_description_trims_and_accepts_the_longest() -> None:
    assert clean_description("  hi ") == "hi"
    longest = "x" * constants.MAX_DESCRIPTION_LENGTH
    assert clean_description(longest) == longest


def test_clean_description_rejects_too_long_text() -> None:
    with pytest.raises(InvalidDetailError):
        clean_description("x" * (constants.MAX_DESCRIPTION_LENGTH + 1))


def test_clean_due_date_accepts_a_date_and_none() -> None:
    assert clean_due_date("2024-02-29") == "2024-02-29"
    assert clean_due_date(None) is None


@pytest.mark.parametrize(
    "raw", ["", "tomorrow", "2023-02-29", "2024-13-01", "20240229", "2024-2-9"]
)
def test_clean_due_date_rejects_a_bad_date(raw: str) -> None:
    with pytest.raises(InvalidDetailError):
        clean_due_date(raw)


def test_clean_comment_trims_and_rejects_empty_and_too_long() -> None:
    assert clean_comment(" ok ") == "ok"
    assert len(clean_comment("x" * constants.MAX_COMMENT_LENGTH)) == (
        constants.MAX_COMMENT_LENGTH
    )
    with pytest.raises(InvalidDetailError):
        clean_comment("   ")
    with pytest.raises(InvalidDetailError):
        clean_comment("x" * (constants.MAX_COMMENT_LENGTH + 1))
