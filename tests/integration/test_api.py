"""Integration tests of the JSON API on a real server."""

from pathlib import Path
from typing import Any

from support.api_client import ApiClient
from support.running_server import running_server
from todo_list import constants


def _board(api: ApiClient) -> dict[str, Any]:
    status, board = api.request("GET", "/api/board")
    assert status == 200
    return dict(board)


def test_get_board_returns_the_default_lists(api: ApiClient) -> None:
    board = _board(api)

    assert [item["name"] for item in board["lists"]] == list(
        constants.DEFAULT_LIST_NAMES
    )


def test_create_rename_and_delete_a_list(api: ApiClient) -> None:
    board_id = _board(api)["id"]

    status, created = api.request(
        "POST", "/api/lists", {"board_id": board_id, "name": " Ideas "}
    )
    assert (status, created["name"]) == (201, "Ideas")

    status, renamed = api.request(
        "PATCH", f"/api/lists/{created['id']}", {"name": "Plans"}
    )
    assert (status, renamed["name"]) == (200, "Plans")

    assert api.request("DELETE", f"/api/lists/{created['id']}") == (204, None)
    names = [item["name"] for item in _board(api)["lists"]]
    assert "Plans" not in names


def test_create_rename_and_delete_a_card(api: ApiClient) -> None:
    list_id = _board(api)["lists"][0]["id"]

    status, created = api.request(
        "POST", f"/api/lists/{list_id}/cards", {"title": "Write"}
    )
    assert (status, created["title"], created["position"]) == (201, "Write", 0)

    status, renamed = api.request(
        "PATCH", f"/api/cards/{created['id']}", {"title": "Wrote"}
    )
    assert (status, renamed["title"]) == (200, "Wrote")
    assert _board(api)["lists"][0]["cards"] == [{"id": created["id"], "title": "Wrote"}]

    assert api.request("DELETE", f"/api/cards/{created['id']}") == (204, None)
    assert _board(api)["lists"][0]["cards"] == []


def test_empty_name_returns_400_with_a_message(api: ApiClient) -> None:
    board_id = _board(api)["id"]

    status, body = api.request(
        "POST", "/api/lists", {"board_id": board_id, "name": "  "}
    )

    assert (status, body["error"]) == (400, constants.ERROR_NAME_EMPTY)


def test_wrong_field_type_returns_400(api: ApiClient) -> None:
    status, body = api.request("POST", "/api/lists", {"board_id": "one", "name": "A"})

    assert status == 400
    assert "board_id" in body["error"]


def test_invalid_json_returns_400_and_no_stack_trace(api: ApiClient) -> None:
    status, text = api.request_raw("POST", "/api/lists", b"{not json")

    assert status == 400
    assert "Traceback" not in text
    assert constants.ERROR_INVALID_JSON in text


def test_unknown_ids_return_404(api: ApiClient) -> None:
    assert api.request("PATCH", "/api/lists/999", {"name": "x"})[0] == 404
    assert api.request("DELETE", "/api/cards/999")[0] == 404
    assert api.request("POST", "/api/lists/999/cards", {"title": "x"})[0] == 404


def test_wrong_method_returns_405(api: ApiClient) -> None:
    assert api.request("DELETE", "/api/board")[0] == 405


def test_added_items_survive_a_server_restart(tmp_path: Path) -> None:
    database = tmp_path / "keep.sqlite3"

    with running_server(database) as url:
        client = ApiClient(url)
        list_id = _board(client)["lists"][0]["id"]
        client.request("POST", f"/api/lists/{list_id}/cards", {"title": "Kept"})

    with running_server(database) as url:
        board = _board(ApiClient(url))

    assert board["lists"][0]["cards"][0]["title"] == "Kept"
