from playwright.sync_api import sync_playwright

from tests.models.inv_add import AddInvoicePage
from tests.models.inv_home import BasePage
from tests.models.inv_nav_menu import NavMenu

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()
    # navigate to home page
    home_page = BasePage(page)
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
    nav_menu.add_invoices_nav()
    add_invoice_page.enter_invoice_detail("invoice1", "company name 1", "builder", "100.00",
                                          "Paid", "2024-01-01", "Plumbing work")
    add_invoice_page.create_invoice_btn()
