"""@brief The composition root: builds the objects and starts the server."""

import logging
from pathlib import Path

from todo_list import constants
from todo_list.application.use_cases.board_use_cases import GetBoard
from todo_list.application.use_cases.card_use_cases import (
    AddComment,
    CreateCard,
    DeleteCard,
    DeleteComment,
    GetCard,
    MoveCard,
    UpdateCardDetails,
)
from todo_list.application.use_cases.list_use_cases import (
    CreateList,
    DeleteList,
    MoveList,
    RenameList,
)
from todo_list.infrastructure.persistence.sqlite_board_repository import (
    SqliteBoardRepository,
)
from todo_list.presentation.features.board.board_controller import BoardController
from todo_list.presentation.features.cards.card_controller import CardController
from todo_list.presentation.features.lists.list_controller import ListController
from todo_list.presentation.http_server import create_server
from todo_list.presentation.router import Router
from todo_list.presentation.routes import build_router


def build_router_for(database_path: Path) -> Router:
    """@brief Wire the store, the use cases and the controllers together.

    @param database_path The SQLite file.
    @return The router of the application.
    """
    repository = SqliteBoardRepository(database_path)
    return build_router(
        BoardController(GetBoard(repository)),
        ListController(
            CreateList(repository),
            RenameList(repository),
            DeleteList(repository),
            MoveList(repository),
        ),
        CardController(
            CreateCard(repository),
            UpdateCardDetails(repository),
            DeleteCard(repository),
            MoveCard(repository),
            GetCard(repository),
            AddComment(repository),
            DeleteComment(repository),
        ),
    )


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
    server = create_server(host, port, build_router_for(database_path))
    logging.info("Serving on http://%s:%s", *server.server_address[:2])
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Stopping")
    finally:
        server.server_close()
