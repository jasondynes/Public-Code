from time import sleep

import pytest
from playwright.sync_api import Page, expect

from models.inv_add import AddInvoicePage
from models.inv_home import HomePage
from models.inv_nav_menu import NavMenu


# fixture to allow test isolation
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each_run(page: Page):
    print("before the test suite runs")
    # go to the starting URL
    page.goto('http://inv.beaufortfairmont.com/#/')
    yield
    print("after the test suite runs")


def test_add_invoice_then_cancel(page: Page):
    # navigate to home page
    home_page = HomePage(page)
    home_page.navigate()
    # select add invoice from LH nav
    nav_menu = NavMenu(page)
    # select 'add invoices' nav option
    nav_menu.add_invoices_nav()
    add_invoice_page = AddInvoicePage(page)
    # enter invoice details
    # TODO: Parameterise call to method and drive from data
    add_invoice_page.enter_invoice_detail("invoice1", "company name 1", "builder", "100.00",
                                          "Paid", "2024-01-01", "Plumbing work")
    add_invoice_page.cancel_invoice_btn()

    # TODO: assert that page.get_by_role("link", name="<invoice num>") does not exist
    # check that invoice does not exist on web page since entry was cancelled
    expect(home_page.find_invoice("invoice1")).to_have_count(0)


def test_add_invoice_then_create(page: Page):
    # navigate to home page
    home_page = HomePage(page)
    home_page.navigate()
    # select add invoice from LH nav
    nav_menu = NavMenu(page)
    # select 'add invoices' nav option
    nav_menu.add_invoices_nav()
    add_invoice_page = AddInvoicePage(page)
    add_invoice_page.enter_invoice_detail("invoice1", "company name 1", "builder", "100.00",
                                          "Paid", "2024-01-01", "Plumbing work")
    add_invoice_page.create_invoice_btn()

    # TODO: check for alert if invoice already exists
    # check that invoice exists on web page
    expect(home_page.find_invoice("invoice1")).to_have_count(1)

    sleep(5)
