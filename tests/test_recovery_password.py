import allure
from utils.urls import Urls
from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestRecoverPassword:
    @allure.title('Проверяем переход по кнопке "Восстановить пароль"')
    @allure.description('Нажимаем на кнопку "Восстановить пароль" и проверяем, что перешли на страницу восстановления'
                        'пароля')
    def test_go_to_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_recover_password()
        url = login_page.current_url()
        assert url == (Urls.MAIN_URL + Urls.RECOVER_PASSWORD)

    @allure.title('Вводим почту и нажимаем на "Восстановить"')
    @allure.description('Вводим почту, нажимаем на "Восстановить" и проверяем переход на страницу смены пароля')
    def test_go_to_reset_page(self, driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.go_to_recover_password()
        recover_page.set_email_and_click_restore()
        url = recover_page.current_url()
        assert url == (Urls.MAIN_URL + Urls.RESET_PASSWORD)

    @allure.title('Вводим новый пароль и нажимаем на кнопку глаза')
    @allure.description('Вводим новый пароль, нажимаем кнопку глаза и проверяем, что пароль стал отображаться')
    def test_show_password_visibility(self, driver):
        recover_page = RecoverPasswordPage(driver)
        recover_page.go_to_recover_password()
        recover_page.set_email_and_click_restore()
        reset_page = ResetPasswordPage(driver)
        reset_page.set_password_and_click_eye_icon()
        response = reset_page.find_input_active()
        assert response.is_displayed() is True
