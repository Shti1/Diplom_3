import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Проверить, что открыта страница восстановления пароля")
    def should_be_forgot_password_page(self):
        self.wait_for_url_contains("/forgot-password")
        self.wait_for_element(ForgotPasswordLocators.RESET_FORM)
        return True

    @allure.step("Ввести email и отправить форму")
    def submit_email_for_reset(self, email):
        self.send_keys_to_input(ForgotPasswordLocators.EMAIL_INPUT, email)
        self.click_on_element(ForgotPasswordLocators.RESET_BUTTON)