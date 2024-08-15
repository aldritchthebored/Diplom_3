import allure
from utils.urls import Urls
from pages.base_page import BasePage
from locators.locators import RecoverPasswordLocators, ResetPasswordLocators


class RecoverPasswordPage(BasePage):
    @allure.step('Перейти на страницу восстановления пароля')
    def go_to_recover_password(self):
        self.go_to_site(Urls.MAIN_URL + Urls.RECOVER_PASSWORD)

    @allure.step('Ввести почту в поле "Email"')
    def set_email(self):
        self.send_keys(RecoverPasswordLocators.EMAIL_FIELD, 'testmail123@ya.ru')

    @allure.step('Нажать на "Восстановить"')
    def click_restore_button(self):
        self.click_element(RecoverPasswordLocators.RECOVER_BUTTON)

    @allure.step('Ввести почту и нажать на кнопку "Восстановить"')
    def set_email_and_click_restore(self):
        self.set_email()
        self.click_restore_button()
        self.find_element(ResetPasswordLocators.EYE_ICON)
