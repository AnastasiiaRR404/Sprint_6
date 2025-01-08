import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт Яндекс самокатов"')
    def go_to_site(self, url="https://qa-scooter.praktikum-services.ru/"):
        self.driver.get(url)

    @allure.step('Нажать на кнопку оформления заказа')
    def click_order_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверить переход на главную страницу')
    def check_switch_on_main_page(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Переключиться на окно Яндекса')
    def switch_on_yandex(self):
        self.switch_to_window()

    @allure.step('Нажать на кнопку вопроса')
    def click_question_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверить текст ответа')
    def check_answer_text(self, answer, expected_text):
        self.wait_for_visibility_of_element(answer)
        actually_text = self.get_actually_text(answer)
        assert actually_text == expected_text

    @allure.step('Нажать на логотип Самоката')
    def click_samokat_logo(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.SAMOKAT_LOGO)
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO)

    @allure.step('Проверить ссылку логотипа Самоката')
    def check_logo_link(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/", "Логотип Самоката не ведёт на главную страницу."