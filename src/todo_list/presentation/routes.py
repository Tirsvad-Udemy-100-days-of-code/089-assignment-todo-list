"""@brief The table of routes: which controller function answers which request."""

from todo_list import constants
from todo_list.presentation.features.board.board_controller import BoardController
from todo_list.presentation.features.cards.card_controller import CardController
from todo_list.presentation.features.lists.list_controller import ListController
from todo_list.presentation.router import Router
from todo_list.presentation.shared.static_files import serve_static


def build_router(
    board: BoardController, lists: ListController, cards: CardController
) -> Router:
    """@brief Register every route of the application.

    @param board The controller of the page and the board data.
    @param lists The controller of the list API.
    @param cards The controller of the card API.
    @return The router.
    """
    router = Router()
    router.add("GET", constants.ROUTE_HOME, board.show_board)
    router.add("GET", constants.STATIC_ROUTE_PREFIX + "{name}", serve_static)
    router.add("GET", "/api/board", board.board_json)
    router.add("POST", "/api/lists", lists.create_list)
    router.add("PATCH", "/api/lists/{id}", lists.rename_list)
    router.add("PATCH", "/api/lists/{id}/move", lists.move_list)
    router.add("DELETE", "/api/lists/{id}", lists.delete_list)
    router.add("POST", "/api/lists/{id}/cards", cards.create_card)
    router.add("PATCH", "/api/cards/{id}", cards.rename_card)
    router.add("PATCH", "/api/cards/{id}/move", cards.move_card)
    router.add("DELETE", "/api/cards/{id}", cards.delete_card)
    return router
