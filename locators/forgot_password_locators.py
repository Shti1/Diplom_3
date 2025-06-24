from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле для ввода email
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")  # Кнопка "Восстановить"
    RESET_FORM = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Заголовок формы сброса
