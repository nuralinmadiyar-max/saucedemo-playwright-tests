from playwright.sync_api import Page

from pages.cart_page import CartPage


class InventoryPage:
    """Страница каталога SauceDemo: локаторы и действия в одном месте."""

    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_names = page.locator('[data-test="inventory-item-name"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def wait_loaded(self):
        """Ждёт, пока на странице появится первый товар."""
        self.item_names.first.wait_for()

    def sort_by(self, option: str):
        """Выбирает сортировку: az, za, lohi или hilo."""
        self.sort_dropdown.select_option(option)

    def get_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def get_prices(self) -> list[float]:
        """Возвращает цены числами: "$29.99" -> 29.99."""
        return [float(price.replace("$", "")) for price in self.item_prices.all_inner_texts()]

    def add_to_cart(self, product_id: str):
        """Нажимает "Add to cart" у товара, например product_id="sauce-labs-backpack"."""
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def open_cart(self) -> CartPage:
        """Открывает корзину и возвращает её Page Object."""
        self.cart_link.click()
        return CartPage(self.page)
