import allure
import pytest

from data import TestData
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
@allure.story("Проверка работы счетчиков в ленте заказов")
@pytest.mark.usefixtures("driver")
class TestFeedPage:
    @allure.title("Проверка открытия деталей заказа в Ленте заказов")
    def test_open_order_details_in_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("1. Перейти в Ленту заказов"):
            main_page.click_order_feed_button()
            assert feed_page.should_be_feed_page()

        with allure.step("2. Кликнуть на первый заказ в ленте"):
            feed_page.click_top_order()

        with allure.step("3. Проверить, что открылось всплывающее окно с деталями"):
            assert feed_page.is_order_details_modal_visible(), "Всплывающее окно не отобразилось"

        with allure.step("4. Проверить, что всплывающее окно содержит текст 'Состав'"):
            assert feed_page.is_composition_text_visible(), "Текст 'Состав' не найден в всплывающем окне"

    @allure.title("Проверка отображения заказов пользователя из раздела 'История заказов' в Ленте заказов")
    def test_user_orders_in_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)
        profile_page = ProfilePage(driver)
        feed_page = FeedPage(driver)

        # 1. Авторизация
        with allure.step("1. Авторизоваться на сайте"):
            main_page.click_login_button()
            login_page.enter_email(TestData.TEST_EMAIL)
            login_page.enter_password(TestData.TEST_PASSWORD)
            login_page.click_login_button()
            assert main_page.should_be_main_page()

        # 2. Создание заказа
        with allure.step("2. Создать тестовый заказ"):
            main_page.drag_ingredient_to_order("Флюоресцентная булка R2-D3")
            main_page.drag_ingredient_to_order("Соус Spicy-X")
            main_page.click_place_order_button()

            # Получаем валидный номер заказа
            order_number = order_page.get_valid_order_number()
            allure.attach(f"Номер заказа: {order_number}", name="Order Number")

            # Закрываем всплывающее окно
            order_page.close_order_modal()

        # 3. Проверка в Истории заказов
        with allure.step("3. Проверить наличие заказа в Истории заказов"):
            main_page.click_personal_account_button()
            profile_page.click_order_history_link()
            assert profile_page.should_be_order_history_page()
            assert profile_page.is_order_in_history(order_number), f"Заказ #{order_number} не найден в Истории заказов"

        # 4. Проверка в Ленте заказов
        with allure.step("4. Проверить наличие заказа в Ленте заказов"):
            main_page.click_order_feed_button()
            assert feed_page.should_be_feed_page()
            assert feed_page.is_order_in_feed(order_number), f"Заказ #{order_number} не найден в Ленте заказов"

            feed_page.click_top_order()
            assert feed_page.is_order_details_modal_visible(), "Не открылось окно деталей заказа"
            assert feed_page.is_composition_text_visible(), "Не найден текст 'Состав' в деталях заказа"

    @allure.title("Проверка увеличения счетчика 'Выполнено за все время' при создании нового заказа")
    def test_order_counter_increases_after_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        order_page = OrderPage(driver)

        # 1. Авторизация
        with allure.step("1. Авторизоваться на сайте"):
            main_page.click_login_button()
            login_page.enter_email(TestData.TEST_EMAIL)
            login_page.enter_password(TestData.TEST_PASSWORD)
            login_page.click_login_button()
            assert main_page.should_be_main_page()

        # 2. Получаем начальное значение счетчика
        with allure.step("2. Получить начальное значение счетчика 'Выполнено за все время'"):
            main_page.click_order_feed_button()
            initial_counter = feed_page.get_all_time_completed_orders_count()
            allure.attach(f"Начальное значение счетчика: {initial_counter}", name="Initial Counter")

        # 3. Создаем новый заказ
        with allure.step("3. Создать тестовый заказ"):
            main_page.click_constructor_button()  # Возвращаемся в конструктор
            main_page.drag_ingredient_to_order("Флюоресцентная булка R2-D3")
            main_page.drag_ingredient_to_order("Соус Spicy-X")
            main_page.click_place_order_button()

            # Получаем номер заказа и закрываем модальное окно
            order_number = order_page.get_valid_order_number()
            allure.attach(f"Номер созданного заказа: {order_number}", name="Order Number")
            order_page.close_order_modal()

        # 4. Проверяем увеличение счетчика
        with allure.step("4. Проверить увеличение счетчика выполненных заказов"):
            main_page.click_order_feed_button()
            is_increased = feed_page.wait_for_counter_increase(initial_counter)
            new_counter = feed_page.get_all_time_completed_orders_count()

            assert is_increased, (
                f"Счетчик не увеличился после создания заказа. "
                f"Было: {initial_counter}, стало: {new_counter}"
            )

    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_counter_increases_after_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        order_page = OrderPage(driver)

        # 1. Авторизация
        with allure.step("1. Авторизоваться на сайте"):
            main_page.click_login_button()
            login_page.enter_email(TestData.TEST_EMAIL)
            login_page.enter_password(TestData.TEST_PASSWORD)
            login_page.click_login_button()
            assert main_page.should_be_main_page()

        # 2. Получаем начальное значение счетчика за сегодня
        with allure.step("2. Получить начальное значение счетчика 'Выполнено за сегодня'"):
            main_page.click_order_feed_button()
            initial_today_count = feed_page.get_today_completed_orders_count()
            allure.attach(f"Начальное значение счетчика за сегодня: {initial_today_count}",
                          name="Initial Today Counter")

        # 3. Создаем новый заказ
        with allure.step("3. Создать тестовый заказ"):
            main_page.click_constructor_button()
            main_page.drag_ingredient_to_order("Флюоресцентная булка R2-D3")
            main_page.drag_ingredient_to_order("Соус Spicy-X")
            main_page.click_place_order_button()

            order_number = order_page.get_valid_order_number()
            allure.attach(f"Номер созданного заказа: {order_number}", name="Order Number")
            order_page.close_order_modal()

        # 4. Проверяем увеличение счетчика за сегодня
        with allure.step("4. Проверить увеличение счетчика 'Выполнено за сегодня'"):
            main_page.click_order_feed_button()
            new_today_count = feed_page.get_today_completed_orders_count()
            allure.attach(f"Новое значение счетчика за сегодня: {new_today_count}",
                          name="New Today Counter")

            assert new_today_count > initial_today_count, (
                f"Счетчик за сегодня не увеличился после создания заказа. "
                f"Было: {initial_today_count}, стало: {new_today_count}"
            )

    @allure.title("Проверка появления номера заказа в разделе 'В работе' после оформления")
    def test_order_appears_in_progress_section(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        order_page = OrderPage(driver)

        # 1. Авторизация
        with allure.step("1. Авторизоваться на сайте"):
            main_page.click_login_button()
            login_page.enter_email(TestData.TEST_EMAIL)
            login_page.enter_password(TestData.TEST_PASSWORD)
            login_page.click_login_button()
            assert main_page.should_be_main_page()

        # 2. Создаем новый заказ
        with allure.step("2. Создать тестовый заказ"):
            main_page.click_constructor_button()
            main_page.drag_ingredient_to_order("Флюоресцентная булка R2-D3")
            main_page.drag_ingredient_to_order("Соус Spicy-X")
            main_page.click_place_order_button()

            # Получаем номер заказа
            order_number = order_page.get_valid_order_number()
            allure.attach(f"Номер созданного заказа: {order_number}", name="Order Number")
            order_page.close_order_modal()

        # 3. Проверяем появление заказа в разделе "В работе"
        with allure.step("3. Проверить появление заказа в разделе 'В работе'"):
            main_page.click_order_feed_button()

            # Ожидаем появления заказа с учетом формата номера (с ведущим нулем)
            expected_number_in_progress = f"0{order_number}"
            feed_page.wait_for_order_in_progress(expected_number_in_progress)

            # Дополнительная проверка для отчетности
            current_orders = feed_page.get_orders_in_progress_numbers()
            allure.attach(f"Текущие заказы в работе: {current_orders}", name="Current Orders")

            assert expected_number_in_progress in current_orders, (
                f"Заказ #{expected_number_in_progress} не найден в разделе 'В работе'. "
                f"Текущие заказы: {current_orders}"
            )