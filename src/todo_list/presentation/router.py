"""@brief The router: maps a method and a path to a controller function."""

import re
from collections.abc import Callable

from todo_list import constants
from todo_list.domain.errors.board_errors import InvalidNameError, NotFoundError
from todo_list.presentation.shared.http_request import BadRequestError, HttpRequest
from todo_list.presentation.shared.http_response import HttpResponse
from todo_list.presentation.shared.json_responses import error_response

Handler = Callable[[HttpRequest], HttpResponse]

_PLACEHOLDERS = {"{id}": r"(?P<id>[0-9]+)", "{name}": r"(?P<name>[A-Za-z0-9_.\-]+)"}


class Router:
    """@brief Holds the routes and answers requests, turning errors into responses."""

    def __init__(self) -> None:
        """@brief Start with no routes."""
        self._routes: list[tuple[str, re.Pattern[str], Handler]] = []

    def add(self, method: str, pattern: str, handler: Handler) -> None:
        """@brief Register a route.

        @param method The HTTP method.
        @param pattern A path that may hold {id} (digits) or {name} (a file name).
        @param handler The controller function.
        """
        regex = re.escape(pattern)
        for placeholder, replacement in _PLACEHOLDERS.items():
            regex = regex.replace(re.escape(placeholder), replacement)
        self._routes.append((method, re.compile(f"^{regex}$"), handler))

    def dispatch(self, method: str, raw_path: str, body: bytes) -> HttpResponse:
        """@brief Answer one request.

        @param method The HTTP method.
        @param raw_path The path, with or without a query string.
        @param body The request body.
        @return The response; 404 for an unknown path, 405 for a wrong method.
        """
        path = raw_path.split("?", 1)[0]
        path_known = False
        for route_method, pattern, handler in self._routes:
            match = pattern.match(path)
            if match is None:
                continue
            path_known = True
            if route_method == method:
                return self._call(
                    handler, HttpRequest(method, path, match.groupdict(), body)
                )
        if path_known:
            return error_response(
                constants.STATUS_METHOD_NOT_ALLOWED, constants.ERROR_METHOD_NOT_ALLOWED
            )
        return error_response(constants.STATUS_NOT_FOUND, constants.ERROR_NOT_FOUND)

    @staticmethod
    def _call(handler: Handler, request: HttpRequest) -> HttpResponse:
        try:
            return handler(request)
        except (BadRequestError, InvalidNameError) as error:
            return error_response(constants.STATUS_BAD_REQUEST, str(error))
        except NotFoundError as error:
            return error_response(constants.STATUS_NOT_FOUND, str(error))
