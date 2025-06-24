import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    @allure.step("Проверить подсветку поля пароля")
    def check_password_field_highlight(self):
        # Ждем исчезновения модального окна (если есть)
        self.wait_for_element_hide(ResetPasswordLocators.MODAL_OVERLAY)

        # Кликаем по кнопке показать/скрыть
        self.click_on_element(ResetPasswordLocators.SHOW_HIDE_BUTTON)

        # Проверяем активное состояние
        self.wait_for_element(ResetPasswordLocators.ACTIVE_PASSWORD_FIELD)
        return True

    @allure.step("Ввести пароль в поле")
    def submit_password_for_reset(self, password):
        self.send_keys_to_input(ResetPasswordLocators.ACTIVE_PASSWORD_INPUT, password)

    @allure.step("Проверить, что открыта страница сброса пароля")
    def should_be_reset_password_page(self):
        self.wait_for_url_contains("/reset-password")
        self.wait_for_element(ResetPasswordLocators.SHOW_HIDE_BUTTON)
        return True