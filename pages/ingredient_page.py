import allure
from locators.ingredient_locators import IngredientLocators
from pages.base_page import BasePage


class IngredientPage(BasePage):
    @allure.step("Проверить что это окно с деталями ингредиента")
    def should_be_ingredient_page(self):
        self.wait_for_url_contains("/ingredient")
        self.wait_for_element(IngredientLocators.INGREDIENT_DETAILS_TITLE)
        return True

    @allure.step("Закрыть всплывающее окно ингредиента")
    def close_ingredient_details_window(self):
        self.wait_for_element(IngredientLocators.CLOSE_BUTTON)
        self.click_on_element(IngredientLocators.CLOSE_BUTTON)

    @allure.step("Проверить видимость окна с ингредиентом")
    def is_modal_content_visible(self):
        self.wait_for_element_hide(IngredientLocators.MODAL_CONTENT)
        return True