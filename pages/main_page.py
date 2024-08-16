import allure
from utils.urls import Urls
from pages.base_page import BasePage
from locators.locators import MainPageLocators, FeedPageLocators


class MainPage(BasePage):
    @allure.step('Перейти на главную')
    def go_to_main(self):
        self.go_to_site(Urls.MAIN_URL)

    @allure.step('Нажать на "Личный Кабинет"')
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_feed_button(self):
        self.click_element(MainPageLocators.FEED_BUTTON)
        self.find_element(FeedPageLocators.FEED_TEXT)

    @allure.step('Нажать на ингридиент "R2-D3"')
    def click_ingredient(self):
        self.click_element(MainPageLocators.BUN)
        self.find_element(MainPageLocators.OPENED_MODAL_BOX)

    @allure.step('Найти окно крестик у "Детали ингредиента"')
    def find_modal_box(self):
        return self.find_clickable_element(MainPageLocators.CLOSE_MODAL_BOX)

    @allure.step('Найти цену у конструктора')
    def find_price(self):
        return self.find_element(MainPageLocators.PRICE_NUMBER)

    @allure.step('Закрыть окно "Детали ингридиента"')
    def close_modal_box(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BOX)
        self.find_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Перетащить ингредиент')
    def add_ingredient(self):
        self.drag_and_drop_ingredient(MainPageLocators.BUN, MainPageLocators.LOWER_HALF_FOR_INGREDIENT)

    @allure.step('Найти каунтер ингредиента "R2-D3"')
    def find_ingredients_counter(self):
        return self.return_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_create_order(self):
        self.click_element(MainPageLocators.CREATE_ORDER)

    @allure.step('Найти модальное окно после оформления заказа')
    def find_order_modal_box(self):
        return self.find_element(MainPageLocators.OPENED_MODAL_BOX)

    @allure.step('Запомнить номер своего заказа')
    def find_number_of_my_order(self):
        self.await_for_invisible_element(MainPageLocators.DEFAULT_NUMBER)
        return self.return_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Закрыть окно заказа')
    def close_order_box(self):
        self.await_for_invisible_element(MainPageLocators.TRASH_ELEMENT)
        element = self.find_element(MainPageLocators.CLOSE_ORDER_BOX)
        self.click_element(element)





