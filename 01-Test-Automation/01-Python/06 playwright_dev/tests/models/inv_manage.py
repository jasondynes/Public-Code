class ManageInvoicePage:
    def __init__(self, page):
        self.page = page
        # invoice number is not editable in screen
        # self.invoice_number = page.get_by_placeholder("Enter invoice number")
        self.company_name = page.get_by_placeholder("Enter company name")
        self.type_of_work = page.get_by_placeholder("Enter type of work")
        self.amount = page.get_by_placeholder("Enter cost")
        self.status = page.locator("#selectStatus")
        self.due_date = page.get_by_placeholder("yyyy-mm-dd")
        self.description = page.locator("input[name=\"comment\"]")
        self.save_invoice = page.get_by_role("button", name="Save")
        self.delete_invoice = page.get_by_role("button", name="Delete Invoice")
        self.cancel_invoice = page.get_by_role("button", name="Cancel")

    def manage_invoice_detail(self, company, work, amount, status, due_date, description):
        self.company_name.fill(company)
        self.type_of_work.fill(work)
        self.amount.fill(amount)
        self.status.select_option(status)
        self.due_date.fill(due_date)
        self.description.fill(description)

    def save_invoice(self):
        self.save_invoice.click()
        
    def delete_invoice(self):
        self.delete_invoice.click()

    def cancel_invoice(self):
        self.cancel_invoice.click()