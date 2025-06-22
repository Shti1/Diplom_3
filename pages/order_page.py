import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_displayed(self):
        return self.wait_for_element(OrderLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text_on_element(OrderLocators.ORDER_NUMBER)

    @allure.step("Получить текст идентификатора заказа")
    def get_order_id_text(self):
        return self.get_text_on_element(OrderLocators.ORDER_ID_TEXT)

    @allure.step("Проверить видимость анимации")
    def is_animation_visible(self):
        return self.wait_for_element(OrderLocators.ANIMATION)

    @allure.step("Получить текст о начале приготовления")
    def get_cooking_text(self):
        return self.get_text_on_element(OrderLocators.COOKING_TEXT)

    @allure.step("Получить текст ожидания")
    def get_waiting_text(self):
        return self.get_text_on_element(OrderLocators.WAITING_TEXT)

    @allure.step("Получить валидный номер заказа (ожидая, пока он станет корректным)")
    def get_valid_order_number(self, timeout=10):
        """Ожидает, пока номер заказа станет корректным (не '9999')"""

        def is_valid_order_number(number):
            return number.isdigit() and number != "9999"

        return WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_order_number() if is_valid_order_number(self.get_order_number()) else False,
            message="Не удалось получить корректный номер заказа"
        )

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.is_order_modal_displayed()
        close_button = self.wait_for_element_to_be_clickable(OrderLocators.MODAL_CLOSE_BUTTON)
        close_button.click()
        self.wait_for_element_hide(OrderLocators.ORDER_MODAL)