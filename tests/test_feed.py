import allure
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPages


class TestFeed:
    @allure.title('Проверяем, что если кликнуть на заказ откроется окно с деталями')
    @allure.description('Пользователь нажимает на заказ и проверяет, что открылось окно с деталями')
    def test_order_modal_box(self, driver):
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        feed_page.click_first_order()
        response = feed_page.find_order_modal_box()
        assert response.is_displayed() is True

    @allure.title('Проверяем, что номер заказа из личного кабинета совпадает с номером на ленте заказов')
    @allure.description('Пользователь делает заказ и сверяет номер из личного кабинета с номером в ленте'
                        'заказов')
    def test_number_of_order(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.add_ingredient()
        main_page.click_create_order()
        main_page.find_order_modal_box()
        main_page.close_order_box()
        main_page.click_personal_account()
        pa_page = PersonalAccountPages(driver)
        pa_page.click_history_of_orders()
        pa_number = pa_page.find_orders_number()
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        fp_number = feed_page.find_numbers_order(pa_number)
        assert pa_number == fp_number

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Пользователь создаёт новый заказ и проверяет, что счётчик за всё время увеличивается')
    def test_counter_for_all_time(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        counter_before = feed_page.find_for_all_time()
        main_page = MainPage(driver)
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.add_ingredient()
        main_page.click_create_order()
        main_page.find_order_modal_box()
        main_page.close_order_box()
        main_page.click_feed_button()
        counter_after = feed_page.find_for_all_time()
        assert counter_before < counter_after

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Пользователь создаёт новый заказ и проверяет, что счётчик за сегодня увеличился')
    def test_for_today(self, driver, create_user):
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        counter_before = feed_page.find_for_today()
        main_page = MainPage(driver)
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.add_ingredient()
        main_page.click_create_order()
        main_page.find_order_modal_box()
        main_page.close_order_box()
        main_page.click_feed_button()
        counter_after = feed_page.find_for_today()
        assert counter_before < counter_after

    @allure.title('Проверяем, что номер заказа находится в работе')
    @allure.description('Пользователь оформляет заказ и проверяет номер своего заказа с номером в разделе "В работе"')
    def test_in_work(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.add_ingredient()
        main_page.click_create_order()
        main_page.find_order_modal_box()
        my_number = main_page.find_number_of_my_order()
        main_page.close_order_box()
        main_page.click_feed_button()
        feed_page = FeedPage(driver)
        feed_page.go_to_feed_page()
        fp_number = feed_page.find_in_work()
        assert my_number in fp_number
