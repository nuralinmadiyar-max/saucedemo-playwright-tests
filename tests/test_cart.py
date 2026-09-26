import re

from playwright.sync_api import expect


def test_added_product_appears_in_cart(inventory_page):
    """Добавленный товар отображается в корзине."""
    inventory_page.add_to_cart("sauce-labs-backpack")
    cart = inventory_page.open_cart()
    expect(cart.item_names).to_have_text(["Sauce Labs Backpack"])


def test_remove_product_from_cart(inventory_page):
    """После удаления товара корзина пустая."""
    inventory_page.add_to_cart("sauce-labs-backpack")
    cart = inventory_page.open_cart()
    cart.remove("sauce-labs-backpack")
    expect(cart.item_names).to_have_count(0)


def test_continue_shopping_returns_to_catalog(inventory_page):
    """Кнопка Continue Shopping возвращает в каталог."""
    cart = inventory_page.open_cart()
    cart.continue_shopping()
    expect(cart.page).to_have_url(re.compile(r".*/inventory\.html"))
