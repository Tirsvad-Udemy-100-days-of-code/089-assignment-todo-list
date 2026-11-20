"""@brief Start the app and save a screenshot of one build step.

Runs inside the container of tools/screenshots/Dockerfile, never on the host
desktop. The repository is mounted at /work; the PNG is written to
docs/screenshots/.

Usage: capture.py <step>   (for example: capture.py step-02)
"""

import sys
import tempfile
import threading
from collections.abc import Callable
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

from todo_list.domain.errors.board_errors import NotFoundError
from todo_list.infrastructure.persistence.sqlite_board_repository import (
    SqliteBoardRepository,
)
from todo_list.main import build_router_for
from todo_list.presentation.http_server import create_server

OUTPUT_DIR = Path("/work/docs/screenshots")
VIEWPORT = {"width": 1280, "height": 720}

DEMO_CARDS = {
    "Backlog": [
        "Plan the release notes",
        "Collect user feedback",
        "Research dark mode",
    ],
    "To Do": [
        "Write the project README",
        "Add the card dialog",
        "Fix the layout on phones",
    ],
    "In Progress": ["Build the drag and drop", "Write the wiki pages"],
    "Review": ["Check the API status codes", "Review the SQLite schema"],
    "Done": [
        "Set up the virtual environment",
        "Create the repository",
        "Choose the stack",
    ],
}


def seed_demo_cards(repository: SqliteBoardRepository) -> None:
    """@brief Fill the default board with sample cards."""
    board = repository.first_board()
    if board is None:
        raise NotFoundError("No board to seed")
    for card_list in repository.lists_of(board.id):
        for title in DEMO_CARDS.get(card_list.name, []):
            repository.add_card(card_list.id, title)


def step_01(page: Page, base_url: str) -> None:
    """@brief Open the first page: the five lists."""
    page.goto(base_url + "/")
    page.wait_for_selector("main.board")


def step_02(page: Page, base_url: str) -> None:
    """@brief Open the board page with sample cards read from SQLite."""
    page.goto(base_url + "/")
    page.wait_for_selector(".card")


def step_03(page: Page, base_url: str) -> None:
    """@brief Add a list and a card through the page, then open a card form."""
    page.set_viewport_size({"width": 1700, "height": 720})
    page.goto(base_url + "/")
    page.wait_for_selector(".card")
    page.get_by_role("button", name="+ Add another list").click()
    page.get_by_label("List name").fill("Ideas")
    page.get_by_role("button", name="Add list").click()
    page.wait_for_selector("h2:text-is('Ideas')")
    todo = page.locator(".list", has=page.locator("h2:text-is('To Do')"))
    todo.get_by_role("button", name="+ Add a card").click()
    todo.get_by_label("Card title").fill("Write the API tests")
    page.evaluate("document.getElementById('board').scrollLeft = 0")


SCENARIOS: dict[str, Callable[[Page, str], None]] = {
    "step-01": step_01,
    "step-02": step_02,
    "step-03": step_03,
}


def main(step: str) -> int:
    """@brief Run one scenario and save its screenshot.

    @param step The scenario name, for example step-02.
    @return The exit code.
    """
    database = Path(tempfile.mkdtemp()) / "shots.sqlite3"
    repository = SqliteBoardRepository(database)
    router = build_router_for(database)
    router.dispatch("GET", "/api/board", b"")  # creates the default board
    if step != "step-01":
        seed_demo_cards(repository)
    server = create_server("127.0.0.1", 0, router)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    host, port = server.server_address[:2]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        SCENARIOS[step](page, f"http://{host!s}:{port}")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(OUTPUT_DIR / f"{step}.png"))
        browser.close()
    server.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
