from selenium.webdriver.common.by import By


class MainLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,
                               "//a[contains(@class, 'AppHeader_header__link')]//p[contains(text(), 'Личный Кабинет')]") # Кнопка "Личный Кабинет"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

    CONSTRUCTOR_BUTTON = (By.XPATH,
                          "//a[contains(@class, 'AppHeader_header__link') and @href='/' and .//p[contains(text(), 'Конструктор')]]") # Кнопка "Конструктор"
    BURGER_CONSTRUCTOR_TITLE = (By.XPATH,
                                "//h1[contains(@class, 'text_type_main-large') and contains(text(), 'Соберите бургер')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href='/feed']") # Кнопка "Лента Заказов"

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка "Оформить заказ"