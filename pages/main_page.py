import allure

from curl import MAIN_SITE
from locators.ingredient_locators import IngredientLocators
from pages.base_page import BasePage
from locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def wait_for_page_loaded(self):
        self.wait_for_element_hide(MainLocators.OVERLAY)

    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.wait_for_page_loaded()
        self.wait_for_element(MainLocators.ENTER_ACCOUNT_BUTTON)
        self.click_on_element(MainLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.wait_for_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_place_order_button(self):
        self.wait_for_page_loaded()
        self.wait_for_element(MainLocators.PLACE_ORDER_BUTTON)
        self.click_on_element(MainLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверить, что это главная страница")
    def should_be_main_page(self):
        """Используем wait_for_url для точного совпадения"""
        self.wait_for_url(f"{MAIN_SITE}/")
        self.wait_for_element(MainLocators.BURGER_CONSTRUCTOR_TITLE)
        return True  # Для удобства использования в assert

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.wait_for_page_loaded()
        self.wait_for_element(MainLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.wait_for_page_loaded()
        self.wait_for_element(MainLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient_details(self):
        self.wait_for_page_loaded()
        self.wait_for_element(IngredientLocators.R2_D3_BUN)
        self.click_on_element(IngredientLocators.R2_D3_BUN)

    @allure.step("Перетащить ингредиент в зону заказа")
    def drag_ingredient_to_order(self, ingredient_name):
        self.wait_for_page_loaded()

        # Получаем локатор из IngredientLocators
        ingredient_locator = IngredientLocators.get_ingredient_locator_by_name(ingredient_name)

        self.wait_for_element(ingredient_locator)
        self.wait_for_element(IngredientLocators.CONSTRUCTOR_DROP_AREA)
        self.drag_and_drop_element(ingredient_locator, IngredientLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self, counter_id):
        counter_locator = IngredientLocators.ingredient_counter(counter_id)
        return self.get_text_on_element(counter_locator)


