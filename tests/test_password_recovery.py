import allure
import pytest


from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
@allure.story("Проверка функционала восстановления пароля")
class TestPasswordRecovery:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_password_recovery(self, driver):
        with allure.step("1. Открыть главную страницу и кликнуть 'Войти в аккаунт'"):
            main_page = MainPage(driver)
            main_page.wait_for_page_loaded() # Явное ожидание загрузки
            main_page.click_login_button()

        with allure.step("2. Проверить переход на страницу логина"):
            login_page = LoginPage(driver)
            assert login_page.should_be_login_page()

        with allure.step("3. Кликнуть 'Восстановить пароль'"):
            login_page.click_forgot_password_link()

        with allure.step("4. Проверить переход на страницу восстановления пароля"):
            forgot_page = ForgotPasswordPage(driver)
            assert forgot_page.should_be_forgot_password_page


    @allure.title("Восстановление пароля по email")
    def test_password_reset_with_email(self, driver, random_email):
        with allure.step("1. Перейти на страницу восстановления пароля"):
            main_page = MainPage(driver)
            main_page.wait_for_page_loaded()
            main_page.click_login_button()

            login_page = LoginPage(driver)
            login_page.click_forgot_password_link()

        with allure.step(f"2. Ввести сгенерированный email ({random_email}) и отправить форму"):
            forgot_password_page = ForgotPasswordPage(driver)
            assert forgot_password_page.should_be_forgot_password_page()
            forgot_password_page.submit_email_for_reset(random_email)

        with allure.step("3. Ожидать загрузки страницы сброса пароля"):
            reset_page = ResetPasswordPage(driver)
            assert reset_page.should_be_reset_password_page

    @allure.title("Проверка подсвечивания поля пароля по кнопке показать/скрыть пароль")
    def test_password_visibility_toggle(self, driver, random_email):
        with allure.step("1. Подготовка: переход на страницу сброса пароля"):
            main_page = MainPage(driver)
            main_page.wait_for_page_loaded()
            main_page.click_login_button()

            login_page = LoginPage(driver)
            login_page.click_forgot_password_link()

            forgot_password_page = ForgotPasswordPage(driver)
            assert forgot_password_page.should_be_forgot_password_page()
            forgot_password_page.submit_email_for_reset(random_email)

        with allure.step("2. Проверка загрузки страницы сброса пароля"):
            reset_page = ResetPasswordPage(driver)
            assert reset_page.should_be_reset_password_page

        with allure.step("3. Проверка подсвечивания поля пароля"):

            assert reset_page.check_password_field_highlight(), \
                "Поле пароля не подсвечивается после клика"