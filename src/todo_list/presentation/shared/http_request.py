"""@brief The request a controller receives from the router."""

import json
from collections.abc import Mapping
from dataclasses import dataclass

from todo_list import constants


class BadRequestError(ValueError):
    """@brief The request is malformed: bad JSON or a wrong field."""


@dataclass(frozen=True)
class HttpRequest:
    """@brief Method, path, path parameters and body of one request.

    @param method The HTTP method, for example GET.
    @param path The path without the query string.
    @param params The values taken from the path pattern, for example id.
    @param body The raw request body.
    """

    method: str
    path: str
    params: Mapping[str, str]
    body: bytes

    def json_object(self) -> dict[str, object]:
        """@brief Parse the body as a JSON object.

        @throws BadRequestError When the body is not a JSON object.
        """
        try:
            data = json.loads(self.body or b"null")
        except (ValueError, UnicodeDecodeError) as error:
            raise BadRequestError(constants.ERROR_INVALID_JSON) from error
        if not isinstance(data, dict):
            raise BadRequestError(constants.ERROR_INVALID_JSON)
        return data

    def path_id(self) -> int:
        """@brief Return the id taken from the path."""
        return int(self.params["id"])


def require_str(data: Mapping[str, object], field: str) -> str:
    """@brief Read a text field of a JSON object.

    @throws BadRequestError When the field is missing or not text.
    """
    value = data.get(field)
    if not isinstance(value, str):
        raise BadRequestError(constants.ERROR_FIELD_MISSING + field)
    return value


def require_int(data: Mapping[str, object], field: str) -> int:
    """@brief Read a whole-number field of a JSON object.

    @throws BadRequestError When the field is missing or not a whole number.
    """
    value = data.get(field)
    if isinstance(value, bool) or not isinstance(value, int):
        raise BadRequestError(constants.ERROR_FIELD_MISSING + field)
    return value
