"""@brief Browser tests of drag and drop (run in the Docker image only)."""

from collections.abc import Callable, Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Locator, Page, ViewportSize, expect, sync_playwright

from support.api_client import ApiClient
from support.running_server import running_server
from todo_list import constants

SEEDED_NAMES = list(constants.DEFAULT_LIST_NAMES)
BACKLOG, TODO = SEEDED_NAMES[0], SEEDED_NAMES[1]
WIDE_VIEWPORT: ViewportSize = {"width": 1280, "height": 800}
NARROW_VIEWPORT: ViewportSize = {"width": 400, "height": 800}

OpenPage = Callable[[ViewportSize], Page]


def _seed_cards(api: ApiClient, list_name: str, titles: list[str]) -> None:
    _, board = api.request("GET", "/api/board")
    list_id = next(item["id"] for item in board["lists"] if item["name"] == list_name)
    for title in titles:
        api.request("POST", f"/api/lists/{list_id}/cards", {"title": title})


@pytest.fixture
def base_url(tmp_path: Path) -> Iterator[str]:
    """@brief The address of a server with a fresh database seeded with cards."""
    with running_server(tmp_path / "dnd.sqlite3") as url:
        api = ApiClient(url)
        _seed_cards(api, BACKLOG, ["A", "B", "C"])
        _seed_cards(api, TODO, ["X"])
        yield url


@pytest.fixture
def open_page(base_url: str) -> Iterator[OpenPage]:
    """@brief A function that opens the board in headless Chromium of a given size."""
    with sync_playwright() as pw:
        browser = pw.chromium.launch()

        def open_at(viewport: ViewportSize) -> Page:
            page = browser.new_page(viewport=viewport)
            page.goto(base_url)
            return page

        yield open_at
        browser.close()


@pytest.fixture
def page(open_page: OpenPage) -> Page:
    """@brief A wide page on the seeded board."""
    return open_page(WIDE_VIEWPORT)


def list_named(page: Page, name: str) -> Locator:
    return page.locator(".list").filter(has=page.get_by_role("heading", name=name))


def card_titles(page: Page, list_name: str) -> Locator:
    return list_named(page, list_name).locator(".card-title")


def list_names(page: Page) -> Locator:
    return page.locator(".list h2")


def test_drag_card_keeps_it_in_the_other_list_when_reloaded(page: Page) -> None:
    card = card_titles(page, BACKLOG).filter(has_text="B")

    card.drag_to(list_named(page, TODO))
    expect(card_titles(page, TODO)).to_have_text(["X", "B"])
    page.reload()

    expect(card_titles(page, BACKLOG)).to_have_text(["A", "C"])
    expect(card_titles(page, TODO)).to_have_text(["X", "B"])


def test_drag_card_keeps_the_new_order_when_reloaded(page: Page) -> None:
    last = card_titles(page, BACKLOG).filter(has_text="C")
    first = card_titles(page, BACKLOG).filter(has_text="A")

    last.drag_to(first, target_position={"x": 5, "y": 1})
    expect(card_titles(page, BACKLOG)).to_have_text(["C", "A", "B"])
    page.reload()

    expect(card_titles(page, BACKLOG)).to_have_text(["C", "A", "B"])


def test_drag_list_keeps_the_new_order_when_reloaded(page: Page) -> None:
    header = list_named(page, BACKLOG).locator(".list-header")
    target = list_named(page, SEEDED_NAMES[4])

    header.drag_to(target, target_position={"x": 5, "y": 5})
    expected = [*SEEDED_NAMES[1:4], BACKLOG, *SEEDED_NAMES[4:]]
    expect(list_names(page)).to_have_text(expected)
    page.reload()

    expect(list_names(page)).to_have_text(expected)


@pytest.mark.parametrize(
    "viewport", [WIDE_VIEWPORT, NARROW_VIEWPORT], ids=["1280", "400"]
)
def test_board_shows_every_list_heading_at_each_viewport_width(
    open_page: OpenPage, viewport: ViewportSize
) -> None:
    page = open_page(viewport)

    expect(list_names(page)).to_have_text(SEEDED_NAMES)
    for name in SEEDED_NAMES:
        expect(page.get_by_role("heading", name=name)).to_have_count(1)
