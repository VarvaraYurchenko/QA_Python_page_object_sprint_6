import allure
import pytest
from pages.main_page import MainPage
from data import TestData


@allure.feature("FAQ")
@allure.story("Раздел 'Вопросы о важном'")
class TestFAQ:
    @allure.title("FAQ: {question}")
    @pytest.mark.parametrize("number, question, expected_answer", TestData.FAQ)
    def test_faq_expand(self, driver, number, question, expected_answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.close_cookie_banner()

        main_page.click_on_faq(number)
        actual_answer = main_page.get_faq_text_answers(number)

        assert actual_answer == expected_answer
