import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    """Открывает страницу логина и отдаёт готовый Page Object."""
    login_page = LoginPage(page)
    login_page.open()
    return login_page
