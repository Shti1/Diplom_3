import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    @allure.step("Проверить, что находимся на странице логина")
    def should_be_login_page(self):
        self.wait_for_url_contains("/login")
        self.wait_for_element(LoginLocators.FORGOT_PASSWORD_LINK)
        return True

    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_on_element(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys_to_input(LoginLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys_to_input(LoginLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_login_button(self):
        self.click_on_element(LoginLocators.LOGIN_BUTTON)