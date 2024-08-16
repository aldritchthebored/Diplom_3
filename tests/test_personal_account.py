import allure
from utils.urls import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPages


class TestPersonalAccount:
    @allure.title('Проверяем переход по кнопке "Личный Кабинет"')
    @allure.description('Нажимаем на кнопку "Личный Кабинет" и проверяем, что перешли в личный кабинет')
    def test_go_to_recovery_page(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.click_personal_account()
        pa_page = PersonalAccountPages(driver)
        pa_page.find_exit_button()
        url = pa_page.current_url()
        assert url == (Urls.MAIN_URL + Urls.PERSONAL_ACCOUNT_URL)

    @allure.title('Проверяем переход в историю заказов пользователя')
    @allure.description('Нажимаем на "История заказов" и проверяем, что кнопка активна')
    def test_history_of_orders(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.click_personal_account()
        pa_page = PersonalAccountPages(driver)
        response = pa_page.click_history_of_orders()
        assert 'Account_link_active' in response

    @allure.title('Проверяем выход из аккаунта')
    @allure.description('Выходим из аккаунта пользователя и проверяем, что открывается страница логина')
    def test_logout(self, driver, create_user):
        main_page = MainPage(driver)
        main_page.go_to_main()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.auth_user(create_user)
        main_page.click_personal_account()
        pa_page = PersonalAccountPages(driver)
        pa_page.click_exit_button()
        url = pa_page.current_url()
        assert url == (Urls.MAIN_URL + Urls.LOGIN_URL)
