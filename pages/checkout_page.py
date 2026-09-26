from playwright.sync_api import Page


class CheckoutPage:
    """Оформление заказа SauceDemo: форма данных, обзор заказа и финальная страница."""

    def __init__(self, page: Page):
        self.page = page
        # Шаг 1: данные покупателя
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.error_message = page.locator('[data-test="error"]')
        # Шаг 2: обзор заказа
        self.item_prices = page.locator('[data-test="inventory-item-price"]')
        self.subtotal_label = page.locator('[data-test="subtotal-label"]')
        self.tax_label = page.locator('[data-test="tax-label"]')
        self.total_label = page.locator('[data-test="total-label"]')
        self.finish_button = page.locator('[data-test="finish"]')
        # Финальная страница
        self.complete_header = page.locator('[data-test="complete-header"]')

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        """Заполняет форму и нажимает Continue."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    @staticmethod
    def amount(label) -> float:
        """Достаёт сумму из текста вида "Item total: $39.98" -> 39.98."""
        label.wait_for()
        return float(label.inner_text().split("$")[1])

    def get_item_prices(self) -> list[float]:
        return [float(price.replace("$", "")) for price in self.item_prices.all_inner_texts()]

    def finish(self):
        self.finish_button.click()
