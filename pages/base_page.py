import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from data import TestData


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TestData.GLOBAL_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element(locator, TestData.GLOBAL_TIMEOUT)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидать конкретный URL")
    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Ожидать, что URL содержит текст")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        drag_and_drop(self.driver, source, target)

    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Ожидает, пока элемент не станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент с локатором {locator} не стал кликабельным за {timeout} секунд"
        )

    @allure.step("Найти элементы по локатору")
    def find_elements(self, locator, timeout=TestData.GLOBAL_TIMEOUT):
        """Возвращает список элементов по локатору"""
        self.wait_for_element(locator, timeout)
        return self.driver.find_elements(*locator)

    @allure.step("Кастомное ожидание условия")
    def custom_wait_until(self, condition, timeout=10, message=""):
        """Ожидает выполнения кастомного условия"""
        return WebDriverWait(self.driver, timeout).until(
            lambda _: condition(),
            message=message
        )

    @allure.step("Кликнуть на элемент через JavaScript")
    def click_via_js(self, locator):
        """Клик по элементу через JavaScript"""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
