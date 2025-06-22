import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    @allure.step("Проверить что это страница ленты заказов")
    def should_be_feed_page(self):
        self.wait_for_url_contains("/feed")
        self.wait_for_element(FeedLocators.ORDER_FEED_TITLE)
        self.wait_for_element(FeedLocators.ALL_TIME_ORDERS)
        self.wait_for_element(FeedLocators.TODAY_ORDERS)
        return True

    @allure.step("Кликнуть на верхний заказ в ленте")
    def click_top_order(self):
        self.click_on_element(FeedLocators.TOP_ORDER)

    @allure.step("Проверить видимость всплывающего окна с деталями заказа")
    def is_order_details_modal_visible(self):
        try:
            return self.wait_for_element(FeedLocators.ORDER_DETAILS_MODAL, timeout=5).is_displayed()
        except:
            return False

    @allure.step("Проверить наличие текста 'Состав' в всплывающем окне")
    def is_composition_text_visible(self):
        try:
            return self.wait_for_element(FeedLocators.COMPOSITION_TEXT, timeout=5).is_displayed()
        except:
            return False

    @allure.step("Найти заказ в Ленте по номеру (без #0)")
    def is_order_in_feed(self, base_number):
        full_number = f"#0{base_number}"
        locator = (FeedLocators.ORDER_IN_FEED_BY_NUMBER[0],
                   FeedLocators.ORDER_IN_FEED_BY_NUMBER[1].replace("starts-with(text(), '#0')", f"text()='{full_number}'"))
        try:
            return self.wait_for_element(locator, timeout=10).is_displayed()
        except:
            return False

    @allure.step("Получить 'сырой' номер из Ленты (формат #0248344)")
    def get_raw_order_number_from_feed(self):
        return self.get_text_on_element(FeedLocators.ORDER_IN_FEED_BY_NUMBER)

    @allure.step("Получить количество выполненных заказов за все время")
    def get_all_time_completed_orders_count(self):
        """Возвращает число из счетчика 'Выполнено за все время'"""
        element = self.wait_for_element(FeedLocators.ALL_TIME_COMPLETED_ORDERS_COUNTER)
        return int(element.text)

    @allure.step("Дождаться увеличения счетчика выполненных заказов")
    def wait_for_counter_increase(self, initial_value, timeout=10):
        """Ожидает увеличения счетчика относительно начального значения"""

        def counter_increased(driver):
            current_value = self.get_all_time_completed_orders_count()
            return current_value > initial_value

        try:
            WebDriverWait(self.driver, timeout).until(
                counter_increased,
                message=f"Счетчик не увеличился за {timeout} секунд. "
                        f"Начальное значение: {initial_value}, текущее: {self.get_all_time_completed_orders_count()}"
            )
            return True
        except TimeoutException:
            return False



    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_completed_orders_count(self):
        """Возвращает число из счетчика 'Выполнено за сегодня'"""
        counter_text = self.get_text_on_element(FeedLocators.TODAY_COMPLETED_ORDERS_COUNTER)
        return int(counter_text) if counter_text.isdigit() else 0

    @allure.step("Получить номера заказов 'В работе'")
    def get_orders_in_progress_numbers(self):
        """Возвращает список номеров заказов в разделе 'В работе'"""
        try:
            elements = self.driver.find_elements(*FeedLocators.ORDER_IN_PROGRESS_NUMBER)
            return [element.text for element in elements if element.text]
        except Exception as e:
            allure.attach(f"Ошибка при получении заказов в работе: {str(e)}", name="Error")
            return []

    @allure.step("Дождаться появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        """Ожидает появления указанного номера заказа в разделе 'В работе'
        :param order_number: номер заказа для проверки (уже в формате с ведущим нулем)
        :param timeout: время ожидания
        """

        def order_is_present(driver):
            try:
                current_orders = self.get_orders_in_progress_numbers()
                return order_number in current_orders
            except Exception:
                return False

        WebDriverWait(self.driver, timeout).until(
            order_is_present,
            message=f"Заказ #{order_number} не появился в разделе 'В работе' за {timeout} сек"
        )
