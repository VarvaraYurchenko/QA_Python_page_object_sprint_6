import pytest
from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Url.main_url)
    yield driver
    driver.quit()