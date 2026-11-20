"""@brief The response a controller hands to the HTTP server."""

from dataclasses import dataclass
from http import HTTPStatus


@dataclass(frozen=True)
class HttpResponse:
    """@brief Status, content type and body of one HTTP response.

    @param status The HTTP status code.
    @param content_type The value of the Content-Type header.
    @param body The response body as text.
    """

    status: HTTPStatus
    content_type: str
    body: str
