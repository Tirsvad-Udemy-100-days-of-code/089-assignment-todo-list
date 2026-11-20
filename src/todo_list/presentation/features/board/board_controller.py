"""@brief The controller of the board page (the C of MVC)."""

from todo_list import constants
from todo_list.application.use_cases.board_use_cases import GetBoard
from todo_list.presentation.features.board.board_view import render_board_page
from todo_list.presentation.shared.http_response import HttpResponse


class BoardController:
    """@brief Answers requests for the board page."""

    def __init__(self, get_board: GetBoard) -> None:
        """@param get_board The use case that reads the board."""
        self._get_board = get_board

    def show_board(self) -> HttpResponse:
        """@brief Build the response for the board page.

        @return A successful HTML response.
        """
        body = render_board_page(constants.APP_TITLE, self._get_board.execute())
        return HttpResponse(constants.STATUS_OK, constants.CONTENT_TYPE_HTML, body)
