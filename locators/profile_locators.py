from selenium.webdriver.common.by import By


class ProfileLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, '/account/order-history')]") # Ссылка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # Ссылка "Выход"

    # Заказ в истории по номеру (динамический)
    ORDER_IN_HISTORY_BY_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#0')]")