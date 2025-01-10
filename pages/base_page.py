import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим значение в поле "{locator}"')
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Нажимаем на элемент "{locator}"')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ожидаем видимость элемента "{locator}"')
    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем кликабельность элемента "{locator}"')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Скроллим к элементу "{locator}"')
    def scroll(self, locator):

        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Получаем текст элемента "{locator}"')
    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.step('Переключаемся на новое окно')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Перейти по ссылке')
    def go_to_url(self, url):
        self.driver.get(url)