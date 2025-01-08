import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from constants_main_page import AnswerConstants
from locators.another_locators import AnotherLocators


@pytest.mark.usefixtures("driver")
class TestLogos:
    @allure.title('Проверка перехода на ya.ru по клику на логотип Yandex')
    def test_yandex_logo(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.click_yandex_logo()
        page.switch_to_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AnotherLocators.SEARCH_FIELD_PLACEHOLDER))
        current_url = page.get_current_url()
        assert "ya.ru" in current_url, "Редирект на главную страницу Яндекса не выполнен."

    @allure.title('Проверка перехода на главную по клике на логотип самоката')
    def test_samokat_logo(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.click_samokat_logo()
        page.check_logo_link()



@pytest.mark.usefixtures("driver")
class TestQuestionPage:
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            (MainPageLocators.PAYMENT_QUESTION_BUTTON, MainPageLocators.PAYMENT_ANSWER, AnswerConstants.PAYMENT_ANSWER),
            (MainPageLocators.SEVERAL_SAMOKAT_QUESTION_BUTTON, MainPageLocators.SEVERAL_SAMOKAT_ANSWER, AnswerConstants.SEVERAL_SAMOKAT_ANSWER),
            (MainPageLocators.RENTAL_TIME_QUESTION_BUTTON, MainPageLocators.RENTAL_TIME_ANSWER, AnswerConstants.RENTAL_TIME_ANSWER),
            (MainPageLocators.ORDER_TODAY_QUESTION_BUTTON, MainPageLocators.ORDER_TODAY_ANSWER, AnswerConstants.ORDER_TODAY_ANSWER),
            (MainPageLocators.LATER_EARLIER_QUESTION_BUTTON, MainPageLocators.LATER_EARLIER_ANSWER, AnswerConstants.LATER_EARLIER_ANSWER),
            (MainPageLocators.CHARGING_QUESTION_BUTTON, MainPageLocators.CHARGING_ANSWER, AnswerConstants.CHARGING_ANSWER),
            (MainPageLocators.CANCEL_QUESTION_BUTTON, MainPageLocators.CANCEL_ANSWER, AnswerConstants.CANCEL_ANSWER),
            (MainPageLocators.LOCATION_QUESTION_BUTTON, MainPageLocators.LOCATION_ANSWER, AnswerConstants.LOCATION_ANSWER)
        ]
    )
    @allure.title('Проверка ответов на вопросы')
    def test_dropdown_list_click_on_button_show_answer_text(self, driver, button, answer, expected_text):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_question_button(button)
        main_page.check_answer_text(answer, expected_text)
