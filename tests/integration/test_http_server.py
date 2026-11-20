"""Integration tests: the page and the static files of a real server."""

import urllib.error
import urllib.request

import pytest

from todo_list import constants


def test_home_returns_the_board_shell(base_url: str) -> None:
    with urllib.request.urlopen(base_url + constants.ROUTE_HOME) as response:
        body = response.read().decode(constants.ENCODING)

        assert response.status == constants.STATUS_OK
        assert response.headers["Content-Type"] == constants.CONTENT_TYPE_HTML
    assert 'id="board"' in body
    assert "/static/app.js" in body


@pytest.mark.parametrize("name", sorted(constants.STATIC_FILES))
def test_static_files_are_served_with_their_content_type(
    base_url: str, name: str
) -> None:
    with urllib.request.urlopen(f"{base_url}/static/{name}") as response:
        assert response.status == constants.STATUS_OK
        assert response.headers["Content-Type"] == constants.STATIC_FILES[name]


def test_unknown_static_file_returns_404(base_url: str) -> None:
    with pytest.raises(urllib.error.HTTPError) as error:
        urllib.request.urlopen(base_url + "/static/secret.txt")

    assert error.value.code == constants.STATUS_NOT_FOUND


def test_unknown_path_returns_404(base_url: str) -> None:
    with pytest.raises(urllib.error.HTTPError) as error:
        urllib.request.urlopen(base_url + "/missing")

    assert error.value.code == constants.STATUS_NOT_FOUND
