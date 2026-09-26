import allure
import pytest
from playwright.sync_api import expect

pytestmark = allure.feature("Оформление заказа")


@pytest.fixture
def checkout_page(inventory_page):
    """Добавляет два товара в корзину и открывает оформление заказа."""
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    return inventory_page.open_cart().checkout()


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Doe", "050000", "Error: First Name is required"),
        ("John", "", "050000", "Error: Last Name is required"),
        ("John", "Doe", "", "Error: Postal Code is required"),
    ],
    ids=["empty_first_name", "empty_last_name", "empty_postal_code"],
)
def test_checkout_form_validation(checkout_page, first_name, last_name, postal_code, expected_error):
    """Пустое обязательное поле в форме показывает ошибку."""
    checkout_page.fill_info(first_name, last_name, postal_code)
    expect(checkout_page.error_message).to_contain_text(expected_error)


def test_order_totals_are_calculated_correctly(checkout_page):
    """Сумма товаров равна сумме цен, итог равен сумме товаров плюс налог."""
    checkout_page.fill_info("John", "Doe", "050000")
    subtotal = checkout_page.amount(checkout_page.subtotal_label)
    tax = checkout_page.amount(checkout_page.tax_label)
    total = checkout_page.amount(checkout_page.total_label)
    assert subtotal == pytest.approx(sum(checkout_page.get_item_prices()))
    assert total == pytest.approx(subtotal + tax)


def test_successful_order(checkout_page):
    """Полный сценарий покупки заканчивается благодарностью за заказ."""
    checkout_page.fill_info("John", "Doe", "050000")
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
