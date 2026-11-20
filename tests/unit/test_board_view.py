"""Unit tests of the board view."""

from todo_list.application.dto.board_dto import BoardDto, CardDto, ListDto
from todo_list.presentation.features.board.board_view import render_board_page


def _board() -> BoardDto:
    backlog = ListDto(1, "Backlog", (CardDto(1, "Write tests"),))
    return BoardDto(1, "My Board", (backlog, ListDto(2, "Done", ())))


def test_render_board_page_shows_title_lists_and_cards() -> None:
    page = render_board_page("Todo List", _board())

    assert "<title>Todo List</title>" in page
    assert page.count('class="list"') == 2
    assert "<h2>Backlog</h2>" in page
    assert '<div class="card">Write tests</div>' in page


def test_render_board_page_escapes_html_in_names() -> None:
    board = BoardDto(1, "B", (ListDto(1, "<script>", (CardDto(1, "<b>x</b>"),)),))

    page = render_board_page("T", board)

    assert "<script>" not in page
    assert "&lt;script&gt;" in page
    assert "&lt;b&gt;x&lt;/b&gt;" in page
