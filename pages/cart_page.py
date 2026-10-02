from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def has_backpack(self) -> bool:
        return self.page.get_by_text("Sauce Labs Backpack").count() == 1

    def start_checkout(self):
        self.page.locator('[data-test="checkout"]').click()
