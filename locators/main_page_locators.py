from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_FOOTER = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    PAYMENT_QUESTION_BUTTON = (By.ID, 'accordion__heading-0')
    PAYMENT_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-0"]/p')
    SEVERAL_SAMOKAT_QUESTION_BUTTON = (By.ID, 'accordion__heading-1')
    SEVERAL_SAMOKAT_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-1"]/p')
    RENTAL_TIME_QUESTION_BUTTON = (By.ID, 'accordion__heading-2')
    RENTAL_TIME_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-2"]/p')
    ORDER_TODAY_QUESTION_BUTTON = (By.ID, 'accordion__heading-3')
    ORDER_TODAY_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-3"]/p')
    LATER_EARLIER_QUESTION_BUTTON = (By.ID, 'accordion__heading-4')
    LATER_EARLIER_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-4"]/p')
    CHARGING_QUESTION_BUTTON = (By.ID, 'accordion__heading-5')
    CHARGING_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-5"]/p')
    CANCEL_QUESTION_BUTTON = (By.ID, 'accordion__heading-6')
    CANCEL_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-6"]/p')
    LOCATION_QUESTION_BUTTON = (By.ID, 'accordion__heading-7')
    LOCATION_ANSWER = (By.XPATH, '//div[@id = "accordion__panel-7"]/p')