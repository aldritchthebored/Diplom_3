import allure
from pages.login_page import LoginPage
from utils.urls import Urls
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainFunctional:
    @allure.title('Проверяем, что авторизированный пользователь может сделать заказ')
    @allure.description('Пользователь входит в профиль и делает заказ на сайте')
    def test_order_modal_box(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.add_ingredient()
        main_page.click_create_order()
        response = main_page.find_order_modal_box()
        assert response.is_displayed() is True

    @allure.title('Проверяем переход по кнопке "Конструктор"')
    @allure.description('Пользователь нажимает на кнопку "Конструктор и проверяет, что он оказался на главной странице')
    def test_go_to_constructor(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        feed_page.click_constructor_button()
        url = feed_page.current_url()
        assert url == Urls.MAIN_URL

    @allure.title('Проверяем переход по кнопке "Лента заказов"')
    @allure.description('Пользователь нажимает на кнопку "Лента заказов" и проверяет, что оказался на странице заказов')
    def test_go_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_feed_button()
        url = main_page.current_url()
        assert url == (Urls.MAIN_URL + Urls.FEED_URL)

    @allure.title('Проверяем, что при нажатии на ингридиент появляется вспылвающее окно')
    @allure.description('Пользователь нажимает на ингридиент и проверяет, что вышло модальное окно с деталями '
                        'ингридиента')
    def test_check_modal_box(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_ingredient()
        response = main_page.find_modal_box()
        assert response.is_displayed() is True

    @allure.title('Проверяем, что при нажатии на крестик закрывается всплывающее окно')
    @allure.description('Пользователь нажимает на крестик у модального окна и проверяет, что оно закрыто')
    def test_check_closing_modal_box(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_ingredient()
        main_page.close_modal_box()
        response = main_page.find_price()
        assert response.is_displayed() is True

    @allure.title('Проверяем, что при добавлении ингридиента увеличивается каунтер данного ингредиента')
    @allure.description('Пользователь добавляет ингридиент и проверяет, что каунтер ингредиента изменился')
    def test_check_the_counter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.add_ingredient()
        response = main_page.find_ingredients_counter()
        assert response == "2"
