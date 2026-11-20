"""@brief The composition root: builds the objects and starts the server."""

import logging
from pathlib import Path

from todo_list import constants
from todo_list.application.use_cases.board_use_cases import GetBoard
from todo_list.infrastructure.persistence.sqlite_board_repository import (
    SqliteBoardRepository,
)
from todo_list.presentation.features.board.board_controller import BoardController
from todo_list.presentation.http_server import create_server


def build_board_controller(database_path: Path) -> BoardController:
    """@brief Wire the store, the use case and the controller together.

    @param database_path The SQLite file.
    @return The controller of the board page.
    """
    return BoardController(GetBoard(SqliteBoardRepository(database_path)))


def main(
    host: str = constants.DEFAULT_HOST,
    port: int = constants.DEFAULT_PORT,
    database_path: Path = Path(constants.DATABASE_FILE_NAME),
) -> None:
    """@brief Start the web server and serve until interrupted.

    @param host The interface to listen on.
    @param port The port to listen on.
    @param database_path The SQLite file.
    """
    logging.basicConfig(level=logging.INFO)
    server = create_server(host, port, build_board_controller(database_path))
    logging.info("Serving on http://%s:%s", *server.server_address[:2])
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Stopping")
    finally:
        server.server_close()
