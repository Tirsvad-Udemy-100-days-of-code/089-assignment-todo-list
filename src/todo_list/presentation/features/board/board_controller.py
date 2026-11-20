"""@brief The controller of the board page (the C of MVC)."""

from todo_list import constants
from todo_list.presentation.features.board.board_view import render_board_page
from todo_list.presentation.shared.http_response import HttpResponse


class BoardController:
    """@brief Answers requests for the board page."""

    def show_board(self) -> HttpResponse:
        """@brief Build the response for the board page.

        @return A successful HTML response.
        """
        body = render_board_page(constants.APP_TITLE, constants.DEFAULT_LIST_NAMES)
        return HttpResponse(constants.STATUS_OK, constants.CONTENT_TYPE_HTML, body)
