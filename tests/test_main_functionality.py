import allure
import pytest

from data import TestData
from pages.feed_page import FeedPage
from pages.ingredient_page import IngredientPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage



@allure.feature("Основной функционал")
@allure.story("Проверка работы Конструктора")
class TestMainFunctionality:
    @allure.title("Переход по клику на Конструктор")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("1. Кликнуть на кнопку 'Конструктор'"):
            main_page.click_constructor_button()

        with allure.step("2. Проверить переход на главную страницу и наличие заголовка 'Соберите бургер'"):
            assert main_page.should_be_main_page()

    @allure.title("Переход по клинку на Лента Заказов")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("1. Кликнуть на кнопку 'Лента Заказов'"):
            main_page.click_order_feed_button()

        with allure.step("2. Проверить переход на страницу Ленты Заказов и наличие заголовков 'Выполнено за все время:' и 'Выполнено за сегодня:'"):
            assert feed_page.should_be_feed_page()

    @allure.title("Открытие окна с деталями при клике на ингредиент и его закрытие по крестику")
    def test_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        ingredient_page = IngredientPage(driver)

        with allure.step("1. Кликнуть на ингредиент Флюоресцентная булка R2-D3"):
            main_page.click_ingredient_details()

        with allure.step(
                "2. Проверить переход на страницу ингредиента и наличие заголовка 'Детали ингредиента'"):
            assert ingredient_page.should_be_ingredient_page()

        with allure.step(
                "3. Закрыть всплывающее окно кликом по крестику"):
            ingredient_page.close_ingredient_details_window()
            assert ingredient_page.is_modal_content_visible()

    @allure.title("Проверка увеличения каунтера при добавлении ингредиента в заказ")
    def test_ingredient_counter_value(self, driver):
        main_page = MainPage(driver)

        with allure.step("1. Проверить начальные значения счетчиков"):
            assert main_page.get_ingredient_counter_value(1) == "0", "Начальный счетчик булки должен быть 0"
            assert main_page.get_ingredient_counter_value(3) == "0", "Начальный счетчик соуса должен быть 0"
            assert main_page.get_ingredient_counter_value(7) == "0", "Начальный счетчик мяса должен быть 0"

        with allure.step("2. Добавить булку R2-D3 в конструктор"):
            main_page.drag_ingredient_to_order(ingredient_name="Флюоресцентная булка R2-D3")
            assert main_page.get_ingredient_counter_value(1) == "2", "Счетчик булки должен стать 2"

        with allure.step("3. Добавить соус Spicy-X в конструктор"):
            main_page.drag_ingredient_to_order(ingredient_name="Соус Spicy-X")
            assert main_page.get_ingredient_counter_value(3) == "1", "Счетчик соуса должен стать 1"

        with allure.step("4. Добавить мясо Protostomia в конструктор"):
            main_page.drag_ingredient_to_order(ingredient_name="Мясо бессмертных моллюсков Protostomia")
            assert main_page.get_ingredient_counter_value(7) == "1", "Счетчик мяса должен стать 1"

    @allure.title("Проверка оформления заказа авторизованным пользователем")
    def test_authenticated_user_can_create_order(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)

        with allure.step("1. Авторизоваться на сайте"):
            main_page.wait_for_page_loaded()
            main_page.click_login_button()
            login_page.enter_email(registered_user['email'])
            login_page.enter_password(registered_user['password'])
            login_page.click_login_button()
            assert main_page.should_be_main_page(), "Не удалось авторизоваться"

        with allure.step("2. Добавить ингредиенты в конструктор"):
            main_page.wait_for_page_loaded()
            main_page.drag_ingredient_to_order("Флюоресцентная булка R2-D3")
            main_page.drag_ingredient_to_order("Соус Spicy-X")
            main_page.drag_ingredient_to_order("Мясо бессмертных моллюсков Protostomia")

        with allure.step("3. Нажать кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
            assert order_page.is_order_modal_displayed(), "Модальное окно заказа не появилось"

        with allure.step("4. Проверить содержимое модального окна заказа"):
            order_number = order_page.get_order_number()
            assert order_number.isdigit(), f"Номер заказа должен быть числом, получено: {order_number}"

            order_id_text = order_page.get_order_id_text().lower()
            assert "идентификатор заказа" in order_id_text

            assert order_page.is_animation_visible(), "Анимация подтверждения не отображается"

            cooking_text = order_page.get_cooking_text()
            assert "начали готовить" in cooking_text

            waiting_text = order_page.get_waiting_text()
            assert "орбитальной станции" in waiting_text


