from selenium import webdriver
from utils.loggers import get_loggers
import pytest
import json


@pytest.fixture(scope="session")
def logger():
    return get_loggers("Test_loggers")


@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as file:
        config = json.load(file)
    return config


@pytest.fixture(scope="function")
def browser(config):
    if config["browser"] == "chrome":
        options = webdriver.ChromeOptions()
        if config["headless"]:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()
    yield driver
    driver.quit()
