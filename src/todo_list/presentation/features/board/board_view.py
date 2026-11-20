"""@brief The view of the board page (the V of MVC)."""

from html import escape

from todo_list.application.dto.board_dto import BoardDto, ListDto

_STYLE = (
    "body{margin:0;font-family:sans-serif;background:#0079bf;color:#172b4d}"
    "header{padding:12px 20px;color:#fff;font-size:20px;font-weight:bold}"
    ".board{display:flex;gap:12px;padding:0 20px;align-items:flex-start}"
    ".list{background:#ebecf0;border-radius:6px;width:260px;padding:8px}"
    ".list h2{font-size:14px;margin:4px 6px 8px}"
    ".card{background:#fff;border-radius:4px;padding:8px;margin:0 0 8px;"
    "box-shadow:0 1px 0 rgba(9,30,66,.25);font-size:14px}"
)


def _render_list(card_list: ListDto) -> str:
    cards = "".join(
        f'<div class="card">{escape(card.title)}</div>' for card in card_list.cards
    )
    return f'<section class="list"><h2>{escape(card_list.name)}</h2>{cards}</section>'


def render_board_page(title: str, board: BoardDto) -> str:
    """@brief Build the HTML of the board page.

    @param title The page title.
    @param board The board with its lists and cards.
    @return The complete HTML document.
    """
    columns = "".join(_render_list(card_list) for card_list in board.lists)
    safe_title = escape(title)
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f"<title>{safe_title}</title><style>{_STYLE}</style></head><body>"
        f"<header>{safe_title}: {escape(board.name)}</header>"
        f'<main class="board">{columns}</main></body></html>'
    )
