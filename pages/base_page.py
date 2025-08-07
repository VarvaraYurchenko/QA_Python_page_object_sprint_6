import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимость элемента")
    def wait_for_element_visible(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_element(self, locator, keys, timeout = 5):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator, timeout = 5):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Переключиться на другую вкладку")
    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать прогрузку страницы")
    def wait_for_url_to_contain(self, url, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    @allure.step("Проверить, что элемент отображается")
    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Подождать, пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))