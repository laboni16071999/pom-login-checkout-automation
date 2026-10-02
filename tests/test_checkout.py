from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_user_can_complete_checkout(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_backpack_and_open_cart()

    cart = CartPage(page)
    assert cart.has_backpack(), "Backpack should appear in the cart"
    cart.start_checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer("QA", "User", "700001")
    checkout.finish_order()

    assert checkout.confirmation_message() == "Thank you for your order!"
