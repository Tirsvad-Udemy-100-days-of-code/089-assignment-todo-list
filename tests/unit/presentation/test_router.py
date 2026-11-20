"""Unit tests of the router."""

from todo_list import constants
from todo_list.domain.errors.board_errors import InvalidNameError, NotFoundError
from todo_list.presentation.router import Router
from todo_list.presentation.shared.http_request import BadRequestError, HttpRequest
from todo_list.presentation.shared.http_response import HttpResponse


def _ok(request: HttpRequest) -> HttpResponse:
    return HttpResponse(constants.STATUS_OK, constants.CONTENT_TYPE_HTML, request.path)


def _raising(error: Exception):  # type: ignore[no-untyped-def]
    def handler(request: HttpRequest) -> HttpResponse:
        raise error

    return handler


def test_dispatch_calls_the_handler_and_ignores_the_query_string() -> None:
    router = Router()
    router.add("GET", "/a", _ok)

    assert router.dispatch("GET", "/a?x=1", b"").body == "/a"


def test_dispatch_passes_path_parameters() -> None:
    router = Router()
    router.add("GET", "/items/{id}", lambda r: HttpResponse(200, "t", r.params["id"]))  # type: ignore[arg-type]

    assert router.dispatch("GET", "/items/42", b"").body == "42"
    assert (
        router.dispatch("GET", "/items/abc", b"").status == constants.STATUS_NOT_FOUND
    )


def test_dispatch_returns_404_for_an_unknown_path() -> None:
    assert Router().dispatch("GET", "/nope", b"").status == constants.STATUS_NOT_FOUND


def test_dispatch_returns_405_for_a_wrong_method() -> None:
    router = Router()
    router.add("GET", "/a", _ok)

    assert (
        router.dispatch("POST", "/a", b"").status == constants.STATUS_METHOD_NOT_ALLOWED
    )


def test_dispatch_maps_errors_to_status_codes() -> None:
    router = Router()
    router.add("GET", "/bad", _raising(BadRequestError("bad")))
    router.add("GET", "/name", _raising(InvalidNameError("name")))
    router.add("GET", "/gone", _raising(NotFoundError("gone")))

    assert router.dispatch("GET", "/bad", b"").status == constants.STATUS_BAD_REQUEST
    assert router.dispatch("GET", "/name", b"").status == constants.STATUS_BAD_REQUEST
    assert router.dispatch("GET", "/gone", b"").status == constants.STATUS_NOT_FOUND
