"""Unit tests of the board view."""

from todo_list.presentation.features.board.board_view import render_board_page


def test_render_board_page_has_title_style_script_and_board() -> None:
    page = render_board_page("Todo List")

    assert "<title>Todo List</title>" in page
    assert 'href="/static/style.css"' in page
    assert 'src="/static/app.js"' in page
    assert 'id="board"' in page


def test_render_board_page_escapes_the_title() -> None:
    page = render_board_page("<script>")

    assert "<script>" not in page.split("</head>")[0]
    assert "&lt;script&gt;" in page
