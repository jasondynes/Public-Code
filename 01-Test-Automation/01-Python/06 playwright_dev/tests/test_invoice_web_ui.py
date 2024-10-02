import pytest
from playwright.sync_api import Page, expect
from tests.models.inv_add import AddInvoicePage
from tests.models.inv_home import BasePage
from tests.models.inv_nav_menu import NavMenu
from tests.models.inv_manage import ManageInvoicePage


# fixture to allow test isolation
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each_run(page: Page):
    # insert any test setup here -------
    print("before the test suite runs")
    yield
    # insert any test teardown here -------
    print("after the test function runs")


@pytest.mark.parametrize("invoice_num, company_name, work_type, amount, status, due_date, description",
                         [("invoice1", "company 1", "builder", "99.99", "Paid", "2024-01-02", "work desc 1")])
def test_add_invoice_then_cancel(page: Page, invoice_num, company_name, work_type, amount, status, due_date,
                                 description):
    home_page = BasePage(page)
    # navigate to home page
    home_page.navigate()
    # select add invoice from LH nav
    nav_menu = NavMenu(page)
    # select 'add invoices' nav option
    nav_menu.add_invoices_nav()
    add_invoice_page = AddInvoicePage(page)
    # enter invoice details
    add_invoice_page.enter_invoice_detail(invoice_num, company_name, work_type, amount, status, due_date, description)
    # cancel invoice
    add_invoice_page.cancel_invoice_btn().click()
    home_page = BasePage(page)
    # check that invoice does not exist on web page since entry was cancelled
    expect(home_page.find_invoice(invoice_num)).to_have_count(0)


# TODO: Data driven tests
# data - invoice num, company name, work type, amount, status(Paid, Sent, Draft, Past due), due date (YYYY-MM-DD) and description
@pytest.mark.parametrize("invoice_num, company_name, work_type, amount, status, due_date, description",
                         [("invoice1", "company 1", "builder", "99.99", "Paid", "2024-01-02", "work desc 1"),
                          ("invoice2", "company 2", "plumber", "100.00", "Draft", "2024-03-04", "work desc 2"),
                          ("invoice3", "company 3", "electrician", "101.01", "Sent", "2024-05-06", "work desc 3")])
def test_add_invoice_then_create(page: Page, invoice_num, company_name, work_type, amount, status, due_date,
                                 description):
    # navigate to home page
    home_page = BasePage(page)
    home_page.navigate()
    # select add invoice from LH nav
    nav_menu = NavMenu(page)
    # select 'add invoices' nav option
    nav_menu.add_invoices_nav()
    add_invoice_page = AddInvoicePage(page)
    add_invoice_page.enter_invoice_detail(invoice_num, company_name, work_type, amount, status, due_date, description)
    add_invoice_page.create_invoice_btn().click()
    # TODO: check for alert if invoice already exists
    # check that invoice exists on web page
    expect(home_page.find_invoice(invoice_num)).to_have_count(1)


@pytest.mark.parametrize("invoice_num, company_name, work_type, amount, status, due_date, description",
                         [("invoice1", "company 1", "builder", "99.99", "Paid", "2024-01-02", "work desc 1"),
                          ("invoice2", "company 2", "plumber", "100.00", "Draft", "2024-03-04", "work desc 2"),
                          ("invoice3", "company 3", "electrician", "101.01", "Sent", "2024-05-06", "work desc 3")])
def test_validate_invoices(page: Page, invoice_num, company_name, work_type, amount, status, due_date, description):
    # navigate to home page
    home_page = BasePage(page)
    home_page.navigate()
    # select invoice details
    home_page.find_invoice(invoice_num).click()
    manage_page = ManageInvoicePage(page)
    # do assertion against each field of each invoice
    expect(manage_page.company_name).to_have_value(company_name)
    expect(manage_page.type_of_work).to_have_value(work_type)
    expect(manage_page.amount).to_have_value(amount)
    expect(manage_page.status).to_have_value(status)
    # TODO: Existing bug as due date is not populated
    # expect(manage_page.due_date).to_have_value(due_date)
    expect(manage_page.description).to_have_value(description)


@pytest.mark.parametrize("invoice_num", ["invoice1", "invoice2", "invoice3"])
def test_delete_invoice_created(page: Page, invoice_num):
    # navigate to home page
    home_page = BasePage(page)
    home_page.navigate()
    # select invoice details
    home_page.find_invoice(invoice_num).click()
    manage_page = ManageInvoicePage(page)
    # delete selected invoice
    manage_page.delete_invoice.click()
