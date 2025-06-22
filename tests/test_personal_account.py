import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from curl import MAIN_SITE


@allure.feature("Личный кабинет")
@allure.story("Проверка функционала личного кабинета")
class TestPersonalAccount:
    @allure.title("Переход по клику в личный кабинет после авторизации")
    def test_navigate_to_personal_account(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("1. Открыть главную страницу и кликнуть 'Войти в аккаунт'"):

            main_page.wait_for_page_loaded()
            main_page.click_login_button()

        with allure.step("2. Заполнить форму авторизации"):

            assert login_page.should_be_login_page()

            login_page.enter_email(registered_user['email'])
            login_page.enter_password(registered_user['password'])
            login_page.click_login_button()

        with allure.step("3. Проверить переход на главную страницу после авторизации"):
            assert main_page.should_be_main_page()

        with allure.step("4. Кликнуть 'Личный кабинет' и проверить переход"):
            main_page.wait_for_page_loaded()
            main_page.click_personal_account_button()

            assert profile_page.should_be_profile_page()

    @allure.title("Переход в раздел 'История заказов'")
    def test_navigate_to_order_history(self, driver, registered_user):
        with allure.step("1. Авторизоваться и перейти в личный кабинет"):
            main_page = MainPage(driver)
            login_page = LoginPage(driver)
            profile_page = ProfilePage(driver)

            main_page.wait_for_page_loaded()
            main_page.click_login_button()

            assert login_page.should_be_login_page()
            login_page.enter_email(registered_user['email'])
            login_page.enter_password(registered_user['password'])
            login_page.click_login_button()

            main_page.wait_for_page_loaded()
            main_page.click_personal_account_button()

            assert profile_page.should_be_profile_page()

        with allure.step("2. Перейти в раздел 'История заказов'"):
            profile_page = ProfilePage(driver)
            profile_page.click_order_history_link()

            assert profile_page.should_be_order_history_page()

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, driver, registered_user):
        with allure.step("1. Авторизоваться и перейти в личный кабинет"):
            main_page = MainPage(driver)
            login_page = LoginPage(driver)
            profile_page = ProfilePage(driver)

            driver.get(MAIN_SITE)
            main_page.wait_for_page_loaded()
            main_page.click_login_button()

            assert login_page.should_be_login_page()
            login_page.enter_email(registered_user['email'])
            login_page.enter_password(registered_user['password'])
            login_page.click_login_button()

            main_page.wait_for_page_loaded()
            main_page.click_personal_account_button()

            assert profile_page.should_be_profile_page()

        with allure.step("2. Выйти из аккаунта"):
            profile_page = ProfilePage(driver)
            profile_page.click_logout_button()

            assert login_page.should_be_login_page()