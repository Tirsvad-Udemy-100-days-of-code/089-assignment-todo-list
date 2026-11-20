"""@brief Builders of JSON responses."""

import json
from dataclasses import asdict, is_dataclass
from http import HTTPStatus

from todo_list import constants
from todo_list.presentation.shared.http_response import HttpResponse


def json_response(status: HTTPStatus, data: object) -> HttpResponse:
    """@brief Build a JSON response.

    @param status The HTTP status.
    @param data A dataclass, or a value that json can write.
    """
    payload = (
        asdict(data) if is_dataclass(data) and not isinstance(data, type) else data
    )
    return HttpResponse(status, constants.CONTENT_TYPE_JSON, json.dumps(payload))


def error_response(status: HTTPStatus, message: str) -> HttpResponse:
    """@brief Build a JSON error response with an error message."""
    return json_response(status, {"error": message})


def no_content() -> HttpResponse:
    """@brief Build an empty 204 response."""
    return HttpResponse(constants.STATUS_NO_CONTENT, constants.CONTENT_TYPE_JSON, "")
