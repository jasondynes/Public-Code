from tests.models.inv_home import BasePage


class AddInvoicePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.invoice_number = page.get_by_placeholder("Enter invoice number")
        self.company_name = page.get_by_placeholder("Enter company name")
        self.type_of_work = page.get_by_placeholder("Enter type of work")
        self.amount = page.get_by_placeholder("Enter cost")
        self.status = page.locator("#selectStatus")
        self.due_date = page.get_by_placeholder("yyyy-mm-dd")
        self.description = page.locator("input[name=\"comment\"]")
        self.create_invoice = page.get_by_role("button", name="Create")
        self.cancel_invoice = page.get_by_role("button", name="Cancel")

    def enter_invoice_detail(self, invoice_num, company, work, amount, status, due_date, description):
        self.invoice_number.fill(invoice_num)
        self.company_name.fill(company)
        self.type_of_work.fill(work)
        self.amount.fill(amount)
        self.status.select_option(status)
        self.due_date.fill(due_date)
        self.description.fill(description)

    def create_invoice_btn(self):
        return self.create_invoice

    def cancel_invoice_btn(self):
        return self.cancel_invoice
