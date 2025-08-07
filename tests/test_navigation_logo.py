import allure
import pytest
from pages.main_page import MainPage
from curl import Urls


@allure.feature("Навигация")
@allure.story("Переходы по логотипам на главной странице")
class TestNavigation:
    @allure.title("Клик по логотипу Самоката возвращает на главную страницу")
    def test_click_on_logo_scooter_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.close_cookie_banner()

        main_page.click_on_order_button_up()
        main_page.click_on_logo_scooter()

        assert main_page.is_main_page_opened()

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_click_on_logo_yandex_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.close_cookie_banner()

        main_page.click_on_logo_yandex()
        main_page.switch_to_dzen_and_wait()

        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url
