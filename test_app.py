from playwright.sync_api import Page, expect


def test_index(page: Page):
    page.goto("http://127.0.0.1:5000")
    # expect(page.locator("body")).to_contain_text("TaskForm")
    # expect(page.locator("p:nth-of-type(1)")).to_contain_text("TaskList")
    # expect(page.locator("p:nth-of-type(2)")).to_contain_text("TaskForm")
    expect(page.locator("p#taskform")).to_contain_text("TaskForm")
