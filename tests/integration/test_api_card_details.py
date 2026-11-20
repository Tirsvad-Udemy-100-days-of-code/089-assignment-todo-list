"""Integration tests of the card detail and comment API."""

from typing import Any

import pytest

from support.api_client import ApiClient


def _new_card(api: ApiClient) -> int:
    _, board = api.request("GET", "/api/board")
    list_id = board["lists"][0]["id"]
    _, card = api.request("POST", f"/api/lists/{list_id}/cards", {"title": "One"})
    return int(card["id"])


def test_patch_sets_details_and_the_board_shows_them(api: ApiClient) -> None:
    card_id = _new_card(api)

    status, card = api.request(
        "PATCH",
        f"/api/cards/{card_id}",
        {"label": "green", "description": "d", "due_date": "2030-01-02", "done": True},
    )
    api.request("POST", f"/api/cards/{card_id}/comments", {"text": "hi"})
    _, board = api.request("GET", "/api/board")

    assert status == 200
    assert (card["label"], card["title"], card["done"]) == ("green", "One", True)
    shown = board["lists"][0]["cards"][0]
    assert (shown["due_date"], shown["comment_count"]) == ("2030-01-02", 1)


def test_patch_with_null_due_date_clears_it(api: ApiClient) -> None:
    card_id = _new_card(api)
    api.request("PATCH", f"/api/cards/{card_id}", {"due_date": "2030-01-02"})

    _, card = api.request("PATCH", f"/api/cards/{card_id}", {"due_date": None})

    assert card["due_date"] is None


def test_comment_lifecycle(api: ApiClient) -> None:
    card_id = _new_card(api)

    status, comment = api.request(
        "POST", f"/api/cards/{card_id}/comments", {"text": " Note "}
    )
    _, details = api.request("GET", f"/api/cards/{card_id}")

    assert (status, comment["text"], comment["card_id"]) == (201, "Note", card_id)
    assert details["comments"] == [comment]
    assert details["comment_count"] == 1
    assert api.request("DELETE", f"/api/comments/{comment['id']}") == (204, None)
    assert api.request("GET", f"/api/cards/{card_id}")[1]["comments"] == []


@pytest.mark.parametrize(
    "body",
    [
        {"label": "pink"},
        {"due_date": "2023-02-30"},
        {"description": "x" * 2001},
        {"title": " "},
        {"done": "yes"},
        {"label": 3},
        {"due_date": 5},
        {},
    ],
)
def test_patch_with_invalid_values_returns_400(
    api: ApiClient, body: dict[str, Any]
) -> None:
    card_id = _new_card(api)

    status, error = api.request("PATCH", f"/api/cards/{card_id}", body)

    assert status == 400
    assert "error" in error


@pytest.mark.parametrize("body", [{"text": " "}, {"text": "x" * 501}, {}])
def test_invalid_comment_returns_400(api: ApiClient, body: dict[str, Any]) -> None:
    card_id = _new_card(api)

    assert api.request("POST", f"/api/cards/{card_id}/comments", body)[0] == 400


def test_unknown_card_or_comment_returns_404(api: ApiClient) -> None:
    assert api.request("GET", "/api/cards/99")[0] == 404
    assert api.request("PATCH", "/api/cards/99", {"done": True})[0] == 404
    assert api.request("POST", "/api/cards/99/comments", {"text": "x"})[0] == 404
    assert api.request("DELETE", "/api/comments/99")[0] == 404
