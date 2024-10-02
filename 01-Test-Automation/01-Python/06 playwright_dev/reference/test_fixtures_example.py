import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")


def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")
    page.goto("https://www.python.org/")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("requests")
    page.get_by_role("button", name="GO").click()
    page.get_by_label("Main Navigation").get_by_role("link", name="Documentation").click()
    page.get_by_role("link", name="Language Reference").click()
    page.get_by_role("link", name="Other tokens").click()
    page.goto("https://www.python.org/")
    expect(page.get_by_label("Main Navigation").get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_label("Main Navigation").get_by_role("link", name="Downloads")).to_be_visible()



