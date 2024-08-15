import allure
from pages.base_page import BasePage
from locators.locators import PersonalAccountLocators, LoginPageLocators


class PersonalAccountPages(BasePage):
    @allure.step('Найти кнопку "Выход"')
    def find_exit_button(self):
        return self.find_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Нажать на кнопку "Выход"')
    def click_exit_button(self):
        self.click_element(PersonalAccountLocators.EXIT_BUTTON)
        self.find_element(LoginPageLocators.RECOVER_PASSWORD)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_of_orders(self):
        self.click_element(PersonalAccountLocators.HISTORY_OF_ORDERS)
        return self.find_element(PersonalAccountLocators.HISTORY_OF_ORDERS).get_attribute('class')

    @allure.step('Найти номер заказа')
    def find_orders_number(self):
        return self.return_text(PersonalAccountLocators.ORDER_NUMBER)
