"""Integration tests of the move endpoints on a real server."""

from typing import Any

from support.api_client import ApiClient

BACKLOG, TODO = 0, 1  # indexes of two seeded lists


def _lists(api: ApiClient) -> list[dict[str, Any]]:
    status, board = api.request("GET", "/api/board")
    assert status == 200
    return list(board["lists"])


def _titles(api: ApiClient, index: int) -> list[str]:
    return [card["title"] for card in _lists(api)[index]["cards"]]


def _add_cards(api: ApiClient, index: int, titles: list[str]) -> list[int]:
    list_id = _lists(api)[index]["id"]
    ids = []
    for title in titles:
        status, card = api.request(
            "POST", f"/api/lists/{list_id}/cards", {"title": title}
        )
        assert status == 201
        ids.append(card["id"])
    return ids


def _list_names(api: ApiClient) -> list[str]:
    return [item["name"] for item in _lists(api)]


def test_move_card_to_another_list_renumbers_both_lists(api: ApiClient) -> None:
    _, b, c = _add_cards(api, BACKLOG, ["A", "B", "C"])
    _add_cards(api, TODO, ["X"])
    todo_id = _lists(api)[TODO]["id"]

    status, moved = api.request(
        "PATCH", f"/api/cards/{b}/move", {"list_id": todo_id, "position": 0}
    )

    assert (status, moved["title"], moved["position"]) == (200, "B", 0)
    assert _titles(api, BACKLOG) == ["A", "C"]
    assert _titles(api, TODO) == ["B", "X"]
    status, again = api.request(
        "PATCH", f"/api/cards/{c}/move", {"list_id": todo_id, "position": 1}
    )
    assert (status, again["position"]) == (200, 1)
    assert _titles(api, TODO) == ["B", "C", "X"]


def test_move_card_within_its_list_changes_the_order(api: ApiClient) -> None:
    a, _, _ = _add_cards(api, BACKLOG, ["A", "B", "C"])
    list_id = _lists(api)[BACKLOG]["id"]

    status, _body = api.request(
        "PATCH", f"/api/cards/{a}/move", {"list_id": list_id, "position": 2}
    )

    assert status == 200
    assert _titles(api, BACKLOG) == ["B", "C", "A"]


def test_move_card_past_the_end_puts_it_at_the_bottom(api: ApiClient) -> None:
    a, _ = _add_cards(api, BACKLOG, ["A", "B"])
    todo_id = _lists(api)[TODO]["id"]
    _add_cards(api, TODO, ["X"])

    status, moved = api.request(
        "PATCH", f"/api/cards/{a}/move", {"list_id": todo_id, "position": 99}
    )

    assert (status, moved["position"]) == (200, 1)
    assert _titles(api, TODO) == ["X", "A"]


def test_move_card_to_a_negative_position_puts_it_on_top(api: ApiClient) -> None:
    _, b = _add_cards(api, BACKLOG, ["A", "B"])
    list_id = _lists(api)[BACKLOG]["id"]

    status, moved = api.request(
        "PATCH", f"/api/cards/{b}/move", {"list_id": list_id, "position": -5}
    )

    assert (status, moved["position"]) == (200, 0)
    assert _titles(api, BACKLOG) == ["B", "A"]


def test_move_card_returns_404_when_the_card_or_list_is_unknown(
    api: ApiClient,
) -> None:
    (card,) = _add_cards(api, BACKLOG, ["A"])
    list_id = _lists(api)[BACKLOG]["id"]

    unknown_card = api.request(
        "PATCH", "/api/cards/999/move", {"list_id": list_id, "position": 0}
    )
    unknown_list = api.request(
        "PATCH", f"/api/cards/{card}/move", {"list_id": 999, "position": 0}
    )

    assert unknown_card[0] == 404
    assert unknown_list[0] == 404
    assert _titles(api, BACKLOG) == ["A"]


def test_move_card_returns_400_when_a_field_has_the_wrong_type(
    api: ApiClient,
) -> None:
    (card,) = _add_cards(api, BACKLOG, ["A"])
    path = f"/api/cards/{card}/move"

    bad_position = api.request("PATCH", path, {"list_id": 1, "position": "0"})
    missing_list = api.request("PATCH", path, {"position": 0})
    bool_position = api.request("PATCH", path, {"list_id": 1, "position": True})

    assert bad_position[0] == 400
    assert "position" in bad_position[1]["error"]
    assert missing_list[0] == 400
    assert "list_id" in missing_list[1]["error"]
    assert bool_position[0] == 400


def test_move_list_right_and_left_changes_the_order(api: ApiClient) -> None:
    original = _list_names(api)
    first_id = _lists(api)[0]["id"]

    status, moved = api.request("PATCH", f"/api/lists/{first_id}/move", {"position": 2})
    assert (status, moved["name"], moved["position"]) == (200, original[0], 2)
    assert _list_names(api) == [original[1], original[2], original[0], *original[3:]]

    status, back = api.request("PATCH", f"/api/lists/{first_id}/move", {"position": 0})
    assert (status, back["position"]) == (200, 0)
    assert _list_names(api) == original


def test_move_list_past_the_end_puts_it_last(api: ApiClient) -> None:
    original = _list_names(api)
    first_id = _lists(api)[0]["id"]

    status, moved = api.request(
        "PATCH", f"/api/lists/{first_id}/move", {"position": 99}
    )

    assert (status, moved["position"]) == (200, len(original) - 1)
    assert _list_names(api) == [*original[1:], original[0]]


def test_move_list_returns_404_when_the_list_is_unknown(api: ApiClient) -> None:
    assert api.request("PATCH", "/api/lists/999/move", {"position": 0})[0] == 404


def test_move_list_returns_400_when_position_has_the_wrong_type(
    api: ApiClient,
) -> None:
    list_id = _lists(api)[0]["id"]
    path = f"/api/lists/{list_id}/move"

    wrong_type = api.request("PATCH", path, {"position": "1"})
    missing = api.request("PATCH", path, {})

    assert wrong_type[0] == 400
    assert "position" in wrong_type[1]["error"]
    assert missing[0] == 400
