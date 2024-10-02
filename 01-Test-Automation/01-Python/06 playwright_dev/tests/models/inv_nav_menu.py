# POM for Nav Menu of invoice app
# Author: Jason Dynes
# Date 26 Sept 2024
from inv_home import BasePage


class NavMenu(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.invoices_nav = page.get_by_role("link", name="Invoices ")
        self.add_invoice_nav = page.get_by_role("link", name="Add Invoice ")
        self.expand_collapse = page.get_by_text("JohnDoe")

    def invoices_nav(self):
        self.invoices_nav.click()

    def add_invoices_nav(self):
        self.add_invoice_nav.click()

    def expand_collapse(self):
        self.expand_collapse.click()
