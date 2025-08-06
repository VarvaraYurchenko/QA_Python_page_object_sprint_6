from selenium.webdriver.common.by import By

class OrderPageLocators:

    # форма 1: Для кого самокат
    NAME = (By.XPATH, "//input[@placeholder='* Имя']") # поле Имя
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле Фамилия
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезём заказ']") # поле Адрес
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле Станция метро
    METRO_STATION_LIST = (By.XPATH, "//div[@class='select-search__row']") # выпадающий список Станций метро
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле Телефон
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']") # кнопка Далее

    # форма 2: Про аренду
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле Дата доставки
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']") # поле Срок аренды
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[text()='сутки']") # выбор Срок аренды на сутки
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']") # выбор Срок аренды на двое суток
    SCOOTER_BLACK_COLOUR = (By.ID, "black") # чекбокс Цвет (самоката) - чёрный
    SCOOTER_GREY_COLOUR = (By.ID, "grey") # чекбокс Цвет (самоката) - серый
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле Комментарий
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") # кнопка Заказать
    BUTTON_YES = (By.XPATH, "//button[text()='Да']") # кнопка Да
    HEADER_SUCCESS = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]") # окно Заказ оформлен
