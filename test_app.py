from playwright.sync_api import Page, expect


def test_has_pebble(page: Page):
    page.goto("http://127.0.0.1:5000")
    expect(page).to_have_title("Hello World")


def test_has_hello_world_text(page: Page):
    page.goto("http://127.0.0.1:5000")
    expect(page.locator("body")).to_contain_text("Testing playwright")
