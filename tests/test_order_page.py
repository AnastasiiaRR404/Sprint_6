import allure
import pytest
from constants_order_page import OrderConstants
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @pytest.mark.parametrize(
        'order_button, customer_data, metro_button, rental_data, days_button, colour_button',
        [
            (
                MainPageLocators.ORDER_BUTTON_HEADER,
                OrderConstants.FIRST_CUSTOMER,
                OrderPageLocators.SELECTOR_METRO1,
                ["2025-01-10", "Коммент"],
                OrderPageLocators.SELECTOR_LEASE_TERM,
                OrderPageLocators.COLOR_BLACK
            ),
            (
                MainPageLocators.ORDER_BUTTON_FOOTER,
                OrderConstants.SECOND_CUSTOMER,
                OrderPageLocators.SELECTOR_METRO2,
                ["2025-01-15", ""],
                OrderPageLocators.FOUR_DAYS_BUTTON,
                OrderPageLocators.COLOR_GREY
            ),
        ]
    )
    @allure.title('Проверка создания заказа')
    def test_make_an_order_data_set_show_success_window(self, driver, order_button, customer_data, metro_button,
                                                        rental_data, days_button, colour_button):
        main_page = MainPage(driver)

        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.fill_out_customer_form(*customer_data, metro_button)
        order_page.click_next_button()

        order_page.fill_out_rental_form(*rental_data, days_button, colour_button)

        order_page.click_order_button()
        order_page.wait_for_load_order_header()
        order_page.click_yes_button()

        order_page.check_success_window()
