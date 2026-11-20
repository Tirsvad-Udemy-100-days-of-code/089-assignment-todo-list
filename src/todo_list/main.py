"""@brief The composition root: builds the objects and starts the server."""

import logging

from todo_list import constants
from todo_list.presentation.features.board.board_controller import BoardController
from todo_list.presentation.http_server import create_server


def main(
    host: str = constants.DEFAULT_HOST, port: int = constants.DEFAULT_PORT
) -> None:
    """@brief Start the web server and serve until interrupted.

    @param host The interface to listen on.
    @param port The port to listen on.
    """
    logging.basicConfig(level=logging.INFO)
    server = create_server(host, port, BoardController())
    logging.info("Serving on http://%s:%s", *server.server_address[:2])
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Stopping")
    finally:
        server.server_close()
