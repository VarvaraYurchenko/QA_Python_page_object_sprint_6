import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку Заказать наверху страницы")
    def click_on_order_button_up(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_UP)

    @allure.step("Кликнуть на кнопку Заказать внизу страницы")
    def click_on_order_button_down(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Кликнуть на логотип Самокат")
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Кликнуть на раздел FAQ 'Вопросы о важном'")
    def click_on_faq(self, question_number):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS[question_number])
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS[question_number])

    @allure.step("Посмотреть ответ в FAQ 'Вопросы о важном'")
    def get_faq_text_answers(self, answer_number):
        self.wait_for_element_visible(MainPageLocators.FAQ_ANSWERS[answer_number])
        return self.get_text_of_element(MainPageLocators.FAQ_ANSWERS[answer_number])

