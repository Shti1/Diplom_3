from selenium.webdriver.common.by import By


class IngredientLocators:
    # Ингредиент
    R2_D3_BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]")
    SPICY_X_SAUCE = (By.XPATH, "//img[contains(@alt, 'Соус Spicy-X')]/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]")
    PROTOSTOMIA_MEAT = (By.XPATH,
                        "//img[contains(@alt, 'Мясо бессмертных моллюсков Protostomia')]/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]")
    # Контейнер контента (всплывающее окно)
    MODAL_CONTENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-30 pb-30')]")
    # Кнопка закрытия (крестик)
    CLOSE_BUTTON = (By.XPATH, "(//button[contains(@class, 'modal__close_modified__') and contains(@class, 'modal__close_')])[1]")
    # Заголовок "Детали ингредиента"
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    # Область конструктора (куда перетаскиваем)
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")

    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")

    @staticmethod
    def ingredient_counter(counter_id):
        """Параметризованный локатор счетчика по порядковому номеру (1-15)"""
        return (By.XPATH, f"(//div[contains(@class, 'counter_counter__')])[{counter_id}]")

    @staticmethod
    def get_ingredient_locator_by_name(ingredient_name):
        """Возвращает локатор для ингредиента по его названию"""
        return (By.XPATH,
                f"//img[contains(@alt, '{ingredient_name}')]/ancestor::a[contains(@class, 'BurgerIngredient_ingredient__')]")