import pytest

from tests.ui.pages.login_page import LoginPage
from utils.config_reader import get_user_by_role


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page, login_page):
    username, password = get_user_by_role("TP Admin")
    LoginPage.login(username, password)
