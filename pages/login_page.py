import allure
from utils.urls import Urls
from pages.base_page import BasePage
from locators.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    @allure.step('Ввести почту')
    def set_email(self, email):
        self.send_keys(LoginPageLocators.LOGIN_EMAIL_INPUT, email)

    @allure.step('Ввести пароль')
    def set_password(self, password):
        self.send_keys(LoginPageLocators.LOGIN_PASSWORD_INPUT, password)

    @allure.step('Нажать на кнопку "Вход"')
    def click_enter_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Переход на страницу входа')
    def go_to_login_page(self):
        self.go_to_site(Urls.MAIN_URL + Urls.LOGIN_URL)

    @allure.step('Нажать на "Восстановить пароль"')
    def click_recover_password(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD)

    @allure.step('Войти в профиль')
    def auth_user(self, create_user):
        email = create_user['email']
        password = create_user['password']
        self.set_email(email)
        self.set_password(password)
        self.click_enter_button()
        self.find_element(MainPageLocators.CREATE_BURGER_TEXT)
