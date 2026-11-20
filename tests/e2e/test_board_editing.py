"""@brief Browser tests of the board editing controls (run in the Docker image only)."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Locator, Page, expect, sync_playwright

from support.running_server import running_server
from todo_list import constants

LIST_NAME = "Backlog"  # a list the board is seeded with
NEW_LIST_NAME = "Extra"
SEEDED_LISTS = len(constants.DEFAULT_LIST_NAMES)
CARD_TITLE = "Buy milk"


@pytest.fixture
def page(tmp_path: Path) -> Iterator[Page]:
    """@brief A headless Chromium page on the board of a fresh database."""
    with running_server(tmp_path / "e2e.sqlite3") as base_url, sync_playwright() as pw:
        browser = pw.chromium.launch()
        browser_page = browser.new_page()
        browser_page.goto(base_url)
        yield browser_page
        browser.close()


def lists(page: Page) -> Locator:
    return page.locator(".list")


def list_named(page: Page, name: str) -> Locator:
    return lists(page).filter(has=page.get_by_role("heading", name=name))


def add_list(page: Page, name: str) -> None:
    page.get_by_role("button", name="+ Add another list").click()
    page.get_by_label("List name").fill(name)
    page.get_by_role("button", name="Add list").click()


def add_card(page: Page, title: str) -> Locator:
    """@brief Add a card to the seeded list and return the list."""
    board_list = list_named(page, LIST_NAME)
    board_list.get_by_role("button", name="+ Add a card").click()
    board_list.get_by_label("Card title").fill(title)
    board_list.get_by_role("button", name="Add", exact=True).click()
    return board_list


def add_card_and_wait(page: Page) -> Locator:
    board_list = add_card(page, CARD_TITLE)
    expect(board_list.locator(".card-title")).to_have_text(CARD_TITLE)
    return board_list


def test_add_list_shows_the_list_when_a_name_is_given(page: Page) -> None:
    add_list(page, NEW_LIST_NAME)

    expect(lists(page)).to_have_count(SEEDED_LISTS + 1)
    expect(list_named(page, NEW_LIST_NAME)).to_have_count(1)


def test_add_card_shows_the_card_when_a_title_is_given(page: Page) -> None:
    board_list = add_card(page, CARD_TITLE)

    expect(board_list.locator(".card-title")).to_have_text(CARD_TITLE)


def test_rename_card_shows_the_new_title_when_saved(page: Page) -> None:
    board_list = add_card_and_wait(page)

    board_list.get_by_role("button", name=f"Rename card {CARD_TITLE}").click()
    board_list.get_by_label("Card title").fill("Buy bread")
    board_list.get_by_role("button", name="Save").click()

    expect(board_list.locator(".card-title")).to_have_text("Buy bread")


def test_delete_card_removes_the_card_when_clicked(page: Page) -> None:
    board_list = add_card_and_wait(page)

    board_list.get_by_role("button", name=f"Delete card {CARD_TITLE}").click()

    expect(page.locator(".card")).to_have_count(0)


def test_add_list_shows_error_when_the_name_is_empty(page: Page) -> None:
    page.get_by_role("button", name="+ Add another list").click()
    page.get_by_label("List name").fill("")
    page.get_by_role("button", name="Add list").click()

    expect(page.locator("#error")).to_have_text(constants.ERROR_NAME_EMPTY)
    expect(lists(page)).to_have_count(SEEDED_LISTS)


def test_reload_keeps_the_added_items_when_the_page_is_reloaded(page: Page) -> None:
    add_list(page, NEW_LIST_NAME)
    expect(list_named(page, NEW_LIST_NAME)).to_have_count(1)
    add_card_and_wait(page)

    page.reload()

    expect(list_named(page, NEW_LIST_NAME)).to_have_count(1)
    expect(page.locator(".card-title")).to_have_text(CARD_TITLE)
