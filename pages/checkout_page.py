from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_customer(self, first_name: str, last_name: str, postal_code: str):
        self.page.locator('[data-test="firstName"]').fill(first_name)
        self.page.locator('[data-test="lastName"]').fill(last_name)
        self.page.locator('[data-test="postalCode"]').fill(postal_code)
        self.page.locator('[data-test="continue"]').click()

    def finish_order(self):
        self.page.locator('[data-test="finish"]').click()

    def confirmation_message(self) -> str:
        return self.page.locator('[data-test="complete-header"]').inner_text()
