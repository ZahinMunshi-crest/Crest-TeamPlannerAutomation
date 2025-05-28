import pytest
from playwright.sync_api import sync_playwright

from utils import config_reader as cr

pytest_plugins = ["fixtures.ui_fixtures", "fixtures.api_fixtures"]


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_name = cr.get_browser_name()
    if browser_name == "chrome":
        browser = playwright_instance.chromium.launch(
            headless=cr.get_headless_mode_status()
        )
    elif browser_name == "firefox":
        browser = playwright_instance.firefox.launch(
            headless=cr.get_headless_mode_status()
        )
    else:
        raise Exception(f"{browser_name} is not supported!")
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
