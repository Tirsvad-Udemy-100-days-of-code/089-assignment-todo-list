"""Integration tests: a real server on a free port with a real database file."""

import threading
import urllib.error
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import pytest

from todo_list import constants
from todo_list.main import build_board_controller
from todo_list.presentation.http_server import create_server


@pytest.fixture
def base_url(tmp_path: Path) -> Iterator[str]:
    controller = build_board_controller(tmp_path / "server.sqlite3")
    server = create_server("127.0.0.1", 0, controller)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address[:2]
    yield f"http://{host!s}:{port}"
    server.shutdown()
    server.server_close()


def test_home_returns_board_with_default_lists(base_url: str) -> None:
    with urllib.request.urlopen(base_url + constants.ROUTE_HOME) as response:
        body = response.read().decode(constants.ENCODING)

        assert response.status == constants.STATUS_OK
    for name in constants.DEFAULT_LIST_NAMES:
        assert f"<h2>{name}</h2>" in body


def test_unknown_path_returns_404(base_url: str) -> None:
    with pytest.raises(urllib.error.HTTPError) as error:
        urllib.request.urlopen(base_url + "/missing")

    assert error.value.code == constants.STATUS_NOT_FOUND
