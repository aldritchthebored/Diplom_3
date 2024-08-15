import allure
from utils.urls import Urls
from pages.base_page import BasePage
from locators.locators import MainPageLocators, FeedPageLocators


class FeedPage(BasePage):
    @allure.step('Переход на страницу "Лента заказов"')
    def go_to_feed_page(self):
        self.go_to_site(Urls.MAIN_URL + Urls.FEED_URL)

    @allure.step('Нажать на кнопку "Конструктор" и найти элемент "Соберите бургер"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        return self.find_element(MainPageLocators.CREATE_BURGER_TEXT)

    @allure.step('Нажать на первый заказ в ленте заказов')
    def click_first_order(self):
        self.click_element(FeedPageLocators.ORDER)

    @allure.step('Найти модальное окно заказа')
    def find_order_modal_box(self):
        return self.find_element(FeedPageLocators.ORDER_MODAL_BOX)

    @allure.step('Найти номер заказа в ленте')
    def find_numbers_order(self, order_id):
        elements = self.find_elements(FeedPageLocators.NUMBER_OF_ORDERS)
        for element in elements:
            if order_id == element.text:
                return element.text

    @allure.step('Найти количество заказов за сегодня')
    def find_for_all_time(self):
        return self.return_text(FeedPageLocators.COUNTER_FOR_ALL_TIME)

    @allure.step('Найти количество заказов за сегодня')
    def find_for_today(self):
        return self.return_text(FeedPageLocators.COUNTER_FOR_TODAY)

    @allure.step('Найти номер заказа в работе')
    def find_in_work(self):
        self.is_element_present(FeedPageLocators.ALL_READY_TEXT)
        self.await_for_invisible_element(FeedPageLocators.ALL_READY_TEXT)
        return self.return_text(FeedPageLocators.IN_WORK)
