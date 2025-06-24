import allure
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):
    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_order_history_link(self):
        self.wait_for_element(ProfileLocators.ORDER_HISTORY_LINK)
        self.click_on_element(ProfileLocators.ORDER_HISTORY_LINK)

    @allure.step("Кликнуть на кнопку 'Выход'")
    def click_logout_button(self):
        self.wait_for_element(ProfileLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfileLocators.LOGOUT_BUTTON)

    @allure.step("Проверить, что это страница профиля")
    def should_be_profile_page(self):
        """Используем wait_for_url_contains для частичного совпадения"""
        self.wait_for_url_contains("/account/profile")
        self.wait_for_element(ProfileLocators.ORDER_HISTORY_LINK) # Дополнительная проверка
        return True

    @allure.step("Проверить, что это страница истории заказов")
    def should_be_order_history_page(self):
        self.wait_for_url_contains("/account/order-history")
        self.wait_for_element(ProfileLocators.ORDER_HISTORY_LINK)  # Дополнительная проверка
        return True

    @allure.step("Найти заказ в Истории по базовому номеру (без #0)")
    def is_order_in_history(self, base_number):
        full_number = f"#0{base_number}"
        locator = (ProfileLocators.ORDER_IN_HISTORY_BY_NUMBER[0],
                   ProfileLocators.ORDER_IN_HISTORY_BY_NUMBER[1].replace("starts-with(text(), '#0')",
                                                                      f"text()='{full_number}'"))
        try:
            return self.wait_for_element(locator, timeout=10).is_displayed()
        except:
            return False