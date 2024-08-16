import allure
from pages.base_page import BasePage
from locators.locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    @allure.step('Ввести пароль')
    def set_password(self):
        self.send_keys(ResetPasswordLocators.NEW_PASSWORD_FIELD, 'newpassword')

    @allure.step('Нажать на иконку глаза')
    def click_eye_icon(self):
        self.click_element(ResetPasswordLocators.EYE_ICON)

    @allure.step('Ввести пароль и нажать на иконку глаза')
    def set_password_and_click_eye_icon(self):
        self.set_password()
        self.click_eye_icon()

    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        return self.find_element(ResetPasswordLocators.ACTIVE_NEW_PASSWORD_FIELD)
