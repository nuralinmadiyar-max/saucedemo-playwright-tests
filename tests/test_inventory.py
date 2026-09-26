import allure
import pytest
from playwright.sync_api import expect

pytestmark = allure.feature("Каталог")


def test_catalog_shows_six_products(inventory_page):
    """После входа в каталоге отображаются 6 товаров."""
    expect(inventory_page.item_names).to_have_count(6)


@pytest.mark.parametrize(
    "option, reverse",
    [("az", False), ("za", True)],
    ids=["name_a_to_z", "name_z_to_a"],
)
def test_sort_by_name(inventory_page, option, reverse):
    """Сортировка по имени упорядочивает товары по алфавиту."""
    expected = sorted(inventory_page.get_names(), reverse=reverse)
    inventory_page.sort_by(option)
    expect(inventory_page.item_names).to_have_text(expected)


@pytest.mark.parametrize(
    "option, reverse",
    [("lohi", False), ("hilo", True)],
    ids=["price_low_to_high", "price_high_to_low"],
)
def test_sort_by_price(inventory_page, option, reverse):
    """Сортировка по цене упорядочивает товары по возрастанию или убыванию."""
    prices = sorted(inventory_page.get_prices(), reverse=reverse)
    expected = [f"${price:.2f}" for price in prices]
    inventory_page.sort_by(option)
    expect(inventory_page.item_prices).to_have_text(expected)


def test_add_one_product_to_cart(inventory_page):
    """После добавления одного товара на значке корзины 1."""
    inventory_page.add_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_add_two_products_to_cart(inventory_page):
    """После добавления двух товаров на значке корзины 2."""
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    expect(inventory_page.cart_badge).to_have_text("2")
