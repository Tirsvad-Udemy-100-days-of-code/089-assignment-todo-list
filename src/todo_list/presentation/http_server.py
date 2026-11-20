"""@brief The HTTP server: maps a request path to a controller."""

import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from todo_list import constants
from todo_list.presentation.features.board.board_controller import BoardController
from todo_list.presentation.shared.http_response import HttpResponse

_LOGGER = logging.getLogger(__name__)


def _not_found() -> HttpResponse:
    return HttpResponse(
        constants.STATUS_NOT_FOUND, constants.CONTENT_TYPE_HTML, "Not found"
    )


def create_server(host: str, port: int, board: BoardController) -> ThreadingHTTPServer:
    """@brief Create, but do not start, the HTTP server.

    @param host The interface to listen on.
    @param port The port to listen on; 0 lets the system choose one.
    @param board The controller of the board page.
    @return The server, ready for serve_forever.
    """

    class Handler(BaseHTTPRequestHandler):
        """@brief Handles the GET requests of one connection."""

        def do_GET(self) -> None:  # noqa: N802 - name fixed by BaseHTTPRequestHandler
            """@brief Answer a GET request."""
            response = (
                board.show_board()
                if self.path == constants.ROUTE_HOME
                else _not_found()
            )
            payload = response.body.encode(constants.ENCODING)
            self.send_response(response.status)
            self.send_header("Content-Type", response.content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, format: str, *args: object) -> None:
            """@brief Send the access log to the logging module."""
            _LOGGER.info(format, *args)

    return ThreadingHTTPServer((host, port), Handler)
