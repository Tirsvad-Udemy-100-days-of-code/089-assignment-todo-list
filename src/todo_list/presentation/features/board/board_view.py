"""@brief The view of the board page (the V of MVC)."""

from collections.abc import Sequence
from html import escape

_STYLE = (
    "body{margin:0;font-family:sans-serif;background:#0079bf;color:#172b4d}"
    "header{padding:12px 20px;color:#fff;font-size:20px;font-weight:bold}"
    ".board{display:flex;gap:12px;padding:0 20px;align-items:flex-start}"
    ".list{background:#ebecf0;border-radius:6px;width:260px;padding:8px}"
    ".list h2{font-size:14px;margin:4px 6px 8px}"
)


def render_board_page(title: str, list_names: Sequence[str]) -> str:
    """@brief Build the HTML of the board page.

    @param title The page title.
    @param list_names The names of the lists, left to right.
    @return The complete HTML document.
    """
    columns = "".join(
        f'<section class="list"><h2>{escape(name)}</h2></section>'
        for name in list_names
    )
    safe_title = escape(title)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{safe_title}</title><style>{_STYLE}</style></head><body>"
        f'<header>{safe_title}</header><main class="board">{columns}</main>'
        "</body></html>"
    )
