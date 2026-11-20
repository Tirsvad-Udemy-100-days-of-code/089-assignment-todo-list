"""@brief Browser tests of the card details dialog (run in the Docker image only)."""

from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Locator, Page, expect, sync_playwright

from support.running_server import running_server

LIST_NAME = "Backlog"  # a list the board is seeded with
CARD_TITLE = "Buy milk"
DUE_DATE = "2099-12-31"
OVERDUE_DATE = "2020-01-01"
DESCRIPTION = "Two litres"


@pytest.fixture
def page(tmp_path: Path) -> Iterator[Page]:
    """@brief A headless Chromium page on a board that has one card."""
    with running_server(tmp_path / "e2e.sqlite3") as base_url, sync_playwright() as pw:
        browser = pw.chromium.launch()
        browser_page = browser.new_page()
        browser_page.goto(base_url)
        board_list = browser_page.locator(".list").first
        board_list.get_by_role("button", name="+ Add a card").click()
        board_list.get_by_label("Card title").fill(CARD_TITLE)
        board_list.get_by_role("button", name="Add", exact=True).click()
        expect(browser_page.locator(".card-title")).to_have_text(CARD_TITLE)
        yield browser_page
        browser.close()


def card(page: Page) -> Locator:
    return page.locator(".card")


def open_dialog(page: Page) -> Locator:
    card(page).locator(".card-body").click()
    dialog = page.locator("dialog.details")
    expect(dialog).to_be_visible()
    return dialog


def save_details(page: Page, due_date: str, *, done: bool = False) -> None:
    dialog = open_dialog(page)
    dialog.get_by_label("Label").select_option("green")
    dialog.get_by_label("Description").fill(DESCRIPTION)
    dialog.get_by_label("Due date").fill(due_date)
    if done:
        dialog.get_by_label("Done").check()
    dialog.get_by_role("button", name="Save").click()
    expect(page.locator("dialog.details")).to_have_count(0)


def test_save_details_shows_badges_when_the_page_is_reloaded(page: Page) -> None:
    save_details(page, DUE_DATE)

    page.reload()

    expect(card(page).locator(".label-bar.label-green")).to_have_count(1)
    expect(card(page).locator(".badge.due")).to_contain_text(DUE_DATE)
    expect(card(page).locator(".badge.description")).to_have_count(1)
    expect(card(page)).not_to_have_class("card overdue")


def test_save_details_marks_the_card_overdue_when_the_due_date_is_past(
    page: Page,
) -> None:
    save_details(page, OVERDUE_DATE)

    expect(card(page)).to_have_class("card overdue")


def test_save_details_crosses_out_the_card_when_done(page: Page) -> None:
    save_details(page, OVERDUE_DATE, done=True)

    expect(card(page)).to_have_class("card done")  # done is never overdue


def test_add_comment_updates_the_count_badge_when_submitted(page: Page) -> None:
    dialog = open_dialog(page)

    dialog.get_by_label("New comment").fill("First note")
    dialog.get_by_role("button", name="Comment", exact=True).click()

    expect(dialog.locator(".comment-text")).to_have_text("First note")
    expect(card(page).locator(".badge.comments")).to_contain_text("1")


def test_delete_comment_removes_the_count_badge_when_clicked(page: Page) -> None:
    dialog = open_dialog(page)
    dialog.get_by_label("New comment").fill("First note")
    dialog.get_by_role("button", name="Comment", exact=True).click()
    expect(card(page).locator(".badge.comments")).to_contain_text("1")

    dialog.get_by_role("button", name="Delete comment").click()

    expect(dialog.locator(".comment")).to_have_count(0)
    expect(card(page).locator(".badge.comments")).to_have_count(0)
