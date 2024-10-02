# POM for Home page of invoice app
# Author: Jason Dynes
# Date 26 Sept 2024

class BasePage:
    def __init__(self, page):
        self.page = page
        self.manage_invoice_nav = page.get_by_role("link", name="Manage")
        self.invoice = None

    def navigate(self):
        self.page.goto('http://inv.beaufortfairmont.com/#/')

    # manage option navigates to edit invoice page
    def manage_nav(self):
        return self.manage_invoice_nav.click()

    def find_invoice(self, invoice_num):
        self.invoice = self.page.get_by_role("link", name=invoice_num)
        return self.invoice

