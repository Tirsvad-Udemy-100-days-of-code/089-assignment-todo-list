"""@brief The view of the board page (the V of MVC)."""

from html import escape


def render_board_page(title: str) -> str:
    """@brief Build the HTML shell of the board page; the script fills the board.

    @param title The page title.
    @return The complete HTML document.
    """
    safe_title = escape(title)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{safe_title}</title><link rel="stylesheet" href="/static/style.css">'
        f'</head><body><header id="title">{safe_title}</header>'
        '<div id="error" role="alert"></div><main id="board" class="board"></main>'
        '<script src="/static/app.js"></script></body></html>'
    )
