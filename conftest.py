import pytest
from selenium import webdriver
from curl import Urls


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()