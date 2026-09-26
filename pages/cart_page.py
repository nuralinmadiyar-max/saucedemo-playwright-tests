from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


class CartPage:
    """Страница корзины SauceDemo."""

    def __init__(self, page: Page):
        self.page = page
        self.item_names = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def remove(self, product_id: str):
        """Удаляет товар из корзины, например product_id="sauce-labs-backpack"."""
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self) -> CheckoutPage:
        """Нажимает Checkout и возвращает страницу оформления заказа."""
        self.checkout_button.click()
        return CheckoutPage(self.page)
