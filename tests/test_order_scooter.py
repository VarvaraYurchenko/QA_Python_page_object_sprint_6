import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий: заполнение формы и подтверждение")
class TestOrderScooter:
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize(
        "user, click_order_btn",
        [
            (TestData.USER_1, MainPage.click_on_order_button_up),
            (TestData.USER_2, MainPage.click_on_order_button_down)
        ]
    )
    def test_order_scooter_with_order_buttons_positive_flow(self, driver, user, click_order_btn):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.close_cookie_banner()

        click_order_btn(main_page)

        order_page.fill_first_form(user)
        order_page.fill_second_form(user)

        order_page.confirm_order()
        assert order_page.is_order_placed()
        assert TestData.SUCCESS_MESSAGE in order_page.get_success_message()
