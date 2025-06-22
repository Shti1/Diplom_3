from selenium.webdriver.common.by import By


class LoginLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input") # Поле "Email"
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']") # Поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, "//form[contains(@class, 'Auth_form')]//button[text()='Войти']") # Кнопка "Войти"