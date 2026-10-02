from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_backpack_and_open_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        self.page.locator(".shopping_cart_link").click()
