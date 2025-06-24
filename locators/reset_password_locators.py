from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    SHOW_HIDE_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
    ACTIVE_PASSWORD_INPUT = (By.CSS_SELECTOR, "div.input_status_active input.input__textfield")
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, "div.input_status_active")