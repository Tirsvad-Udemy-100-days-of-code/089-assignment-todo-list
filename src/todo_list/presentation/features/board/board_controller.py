"""@brief The controller of the board page and the board API (the C of MVC)."""

from todo_list import constants
from todo_list.application.use_cases.board_use_cases import GetBoard
from todo_list.presentation.features.board.board_view import render_board_page
from todo_list.presentation.shared.http_request import HttpRequest
from todo_list.presentation.shared.http_response import HttpResponse
from todo_list.presentation.shared.json_responses import json_response


class BoardController:
    """@brief Answers requests for the board page and the board data."""

    def __init__(self, get_board: GetBoard) -> None:
        """@param get_board The use case that reads the board."""
        self._get_board = get_board

    def show_board(self, request: HttpRequest) -> HttpResponse:
        """@brief Build the response for the board page."""
        body = render_board_page(constants.APP_TITLE)
        return HttpResponse(constants.STATUS_OK, constants.CONTENT_TYPE_HTML, body)

    def board_json(self, request: HttpRequest) -> HttpResponse:
        """@brief Build the JSON of the whole board."""
        return json_response(constants.STATUS_OK, self._get_board.execute())
