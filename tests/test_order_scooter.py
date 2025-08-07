import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий: заполнение формы и подтверждение")
class TestOrderScooter:
    @allure.title("Заказ: {user['name']} {user['last_name']} — кнопка '{button}'")
    @pytest.mark.parametrize("user, button",
                             [(TestData.USER_1, "up"),
                              (TestData.USER_2, "down")])
    def test_order_scooter_with_order_buttons_positive_flow(self, driver, user, button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.close_cookie_banner()

        if button == "up":
            main_page.click_on_order_button_up()
        else:
            main_page.click_on_order_button_down()

        order_page.fill_first_form(user)
        order_page.fill_second_form(user)

        order_page.confirm_order()
        assert order_page.is_order_placed()
        assert "Заказ оформлен" in order_page.get_success_message()
