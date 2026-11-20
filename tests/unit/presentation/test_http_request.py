"""Unit tests of the request and its field helpers."""

import pytest

from todo_list.presentation.shared.http_request import (
    BadRequestError,
    HttpRequest,
    require_int,
    require_str,
)


def _request(body: bytes, **params: str) -> HttpRequest:
    return HttpRequest("POST", "/x", params, body)


def test_json_object_parses_an_object() -> None:
    assert _request(b'{"a": 1}').json_object() == {"a": 1}


@pytest.mark.parametrize("body", [b"", b"[1]", b"{broken", b"\xff\xfe"])
def test_json_object_rejects_anything_else(body: bytes) -> None:
    with pytest.raises(BadRequestError):
        _request(body).json_object()


def test_path_id_reads_the_id_parameter() -> None:
    assert _request(b"", id="7").path_id() == 7


def test_require_str_and_require_int_accept_the_right_types() -> None:
    assert require_str({"a": "x"}, "a") == "x"
    assert require_int({"a": 3}, "a") == 3


@pytest.mark.parametrize("value", [None, 1, True])
def test_require_str_rejects_other_types(value: object) -> None:
    with pytest.raises(BadRequestError):
        require_str({"a": value}, "a")


@pytest.mark.parametrize("value", [None, "1", True, 1.5])
def test_require_int_rejects_other_types(value: object) -> None:
    with pytest.raises(BadRequestError):
        require_int({"a": value}, "a")
