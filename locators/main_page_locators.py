from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_UP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']") # кнопка Заказать наверху страницы
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # кнопка Заказать внизу страницы

    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR") # кнопка-логотип Самокат
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") # кнопка-логотип Яндекс

    # раздел FAQ "Вопросы о важном", ВОПРОСЫ
    FAQ_QUESTIONS = {
        1: (By.ID, "accordion__heading-0"),
        2: (By.ID, "accordion__heading-1"),
        3: (By.ID, "accordion__heading-2"),
        4: (By.ID, "accordion__heading-3"),
        5: (By.ID, "accordion__heading-4"),
        6: (By.ID, "accordion__heading-5"),
        7: (By.ID, "accordion__heading-6"),
        8: (By.ID, "accordion__heading-7")
    }

    # раздел FAQ "Вопросы о важном", ОТВЕТЫ
    FAQ_ANSWERS = {
        1: (By.ID, "accordion__panel-0"),
        2: (By.ID, "accordion__panel-1"),
        3: (By.ID, "accordion__panel-2"),
        4: (By.ID, "accordion__panel-3"),
        5: (By.ID, "accordion__panel-4"),
        6: (By.ID, "accordion__panel-5"),
        7: (By.ID, "accordion__panel-6"),
        8: (By.ID, "accordion__panel-7")
    }
