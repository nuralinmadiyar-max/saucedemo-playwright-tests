"""Тесты на известные дефекты SauceDemo.

У пользователей problem_user и error_user сайт намеренно сломан. Тесты описывают
правильное поведение, поэтому падают из-за дефекта и помечены как xfail.
strict=True: если дефект когда-нибудь исправят, тест пройдёт и pytest сообщит об этом.
"""
import re

import allure
import pytest
from playwright.sync_api import expect

pytestmark = allure.feature("Известные дефекты")


@pytest.mark.xfail(strict=True, reason="BUG: у problem_user у всех товаров одна и та же картинка")
def test_problem_user_products_have_unique_images(login_as):
    """У каждого из 6 товаров должна быть своя картинка."""
    inventory = login_as("problem_user")
    expect(inventory.item_images).to_have_count(6)
    assert len(set(inventory.get_image_sources())) == 6


@pytest.mark.xfail(strict=True, reason="BUG: у problem_user сортировка по имени не меняет порядок товаров")
def test_problem_user_sort_by_name_z_to_a(login_as):
    """Сортировка Z→A должна упорядочить товары по алфавиту в обратном порядке."""
    inventory = login_as("problem_user")
    expected = sorted(inventory.get_names(), reverse=True)
    inventory.sort_by("za")
    expect(inventory.item_names).to_have_text(expected)


@pytest.mark.xfail(strict=True, reason="BUG: у problem_user кнопка Add to cart не работает для части товаров")
def test_problem_user_add_bolt_t_shirt_to_cart(login_as):
    """Добавление футболки Bolt T-Shirt должно показать 1 на значке корзины."""
    inventory = login_as("problem_user")
    inventory.add_to_cart("sauce-labs-bolt-t-shirt")
    expect(inventory.cart_badge).to_have_text("1")


@pytest.mark.xfail(strict=True, reason="BUG: у problem_user ввод в поле Last Name попадает в поле First Name")
def test_problem_user_checkout_form_accepts_last_name(login_as):
    """Заполненная форма должна вести на шаг обзора заказа."""
    inventory = login_as("problem_user")
    inventory.add_to_cart("sauce-labs-backpack")
    checkout = inventory.open_cart().checkout()
    checkout.fill_info("John", "Doe", "050000")
    expect(checkout.page).to_have_url(re.compile(r".*/checkout-step-two\.html"))


@pytest.mark.xfail(strict=True, reason="BUG: у error_user сортировка выдаёт ошибку и не меняет порядок товаров")
def test_error_user_sort_by_name_z_to_a(login_as):
    """Сортировка Z→A должна упорядочить товары по алфавиту в обратном порядке."""
    inventory = login_as("error_user")
    expected = sorted(inventory.get_names(), reverse=True)
    inventory.sort_by("za")
    expect(inventory.item_names).to_have_text(expected)


@pytest.mark.xfail(strict=True, reason="BUG: у error_user оформление заказа не завершается")
def test_error_user_can_complete_order(login_as):
    """Полный сценарий покупки должен закончиться благодарностью за заказ."""
    inventory = login_as("error_user")
    inventory.page.set_default_timeout(5000)
    inventory.add_to_cart("sauce-labs-backpack")
    checkout = inventory.open_cart().checkout()
    checkout.fill_info("John", "Doe", "050000")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
