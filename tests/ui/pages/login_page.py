from utils.config_reader import get_ui_url

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = get_ui_url("login")

    @property
    def username_input(self):
        return self.page.get_by_role("textbox", name="Username")

    @property
    def password_input(self):
        return self.page.get_by_role("textbox", name="Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def timesheet_header(self):
        return self.page.get_by_text("My Timesheet")

    @property
    def login_error_message(self):
        return self.page.locator(".login-error")

    def open(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
