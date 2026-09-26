from playwright.sync_api import Page


class LoginPage:
    """Страница логина SauceDemo: локаторы и действия в одном месте."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
