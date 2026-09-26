import allure
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    """Открывает страницу логина и отдаёт готовый Page Object."""
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(login_page):
    """Входит под standard_user и отдаёт страницу каталога."""
    login_page.login("standard_user", PASSWORD)
    inventory_page = InventoryPage(login_page.page)
    inventory_page.wait_loaded()
    return inventory_page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Если тест упал, прикрепляет скриншот страницы к Allure-отчёту."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            allure.attach(
                page.screenshot(full_page=True),
                name="Скриншот при падении",
                attachment_type=allure.attachment_type.PNG,
            )
