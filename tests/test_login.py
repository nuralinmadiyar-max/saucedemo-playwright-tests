import re

import allure
import pytest
from playwright.sync_api import expect

pytestmark = allure.feature("Логин")


PASSWORD = "secret_sauce"


def test_successful_login(login_page):
    """Успешный вход с валидными данными ведёт в каталог."""
    login_page.login("standard_user", PASSWORD)
    expect(login_page.page).to_have_url(re.compile(r".*/inventory\.html"))


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        ("locked_out_user", PASSWORD, "Epic sadface: Sorry, this user has been locked out."),
        ("wrong_user", "wrong_pass",
         "Epic sadface: Username and password do not match any user in this service"),
    ],
    ids=["empty_fields", "empty_password", "locked_out_user", "invalid_credentials"],
)
def test_login_error(login_page, username, password, expected_error):
    """Негативные сценарии входа показывают правильное сообщение об ошибке."""
    login_page.login(username, password)
    expect(login_page.error_message).to_contain_text(expected_error)
