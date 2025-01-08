from selenium.webdriver.common.by import By


class OrderPageLocators:
    SELECTOR_METRO1 = [By.XPATH, './/*[text() = "Черкизовская"]']
    SELECTOR_METRO2 = [By.XPATH, './/*[text() = "Сокольники"]']
    NAME_FIELD = (By.XPATH, '//input[@placeholder = "* Имя"]')
    LASTNAME_FIELD = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE_CALENDAR = (By.XPATH, './/div[@class = "react-datepicker__month"]/div[last()]/div[last()]')
    SELECTOR_LEASE_TERM = [By.XPATH, './/*[text() = "сутки"]']
    TIME_RENT_INPUT = [By.XPATH, './/div[text() = "* Срок аренды"]']
    COLOR_BLACK = [By.XPATH, './/input[@id = "black"]']
    COLOR_GREY = [By.XPATH, './/input[@id = "grey"]']
    COMMENT = [By.XPATH, './/div/input[@placeholder = "Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, './/div[@class = "Order_Buttons__1xGrp"]/button[text()= "Заказать"]']
    CONFIRMATION_BUTTON = [By.XPATH, './/button[text() = "Да"]']
    CONFIRMATION_HEADER = [By.XPATH, './/div[@class = "Order_ModalHeader__3FDaJ"]']
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    RENTAL_HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')
    FOUR_DAYS_BUTTON = (By.XPATH, '//div[text() = "четверо суток"]')
    BUTTON_ON_SUCCESS_WINDOW = (By.XPATH, '//button[text()="Посмотреть статус"]')
    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    METRO_FIELD = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')