"""Unit tests of the board view."""

from todo_list.presentation.features.board.board_view import render_board_page


def test_render_board_page_shows_title_and_every_list() -> None:
    page = render_board_page("Todo List", ["Backlog", "Done"])

    assert "<title>Todo List</title>" in page
    assert page.count('class="list"') == 2
    assert "<h2>Backlog</h2>" in page


def test_render_board_page_escapes_html_in_names() -> None:
    page = render_board_page("T", ["<script>"])

    assert "<script>" not in page
    assert "&lt;script&gt;" in page
