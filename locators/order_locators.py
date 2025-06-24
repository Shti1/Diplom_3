from selenium.webdriver.common.by import By


class OrderLocators:
    # Модальное окно подтверждения заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-30 pb-30')]")
    # Локатор для основного контейнера модального окна заказа

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    # Локатор для номера заказа (крупные цифры)

    ORDER_ID_TEXT = (By.XPATH, "//p[contains(@class, 'text_type_main-medium')]")
    # Локатор для текста "идентификатор заказа" под номером

    ANIMATION = (By.XPATH, "//img[contains(@class, 'Modal_modal__image__2nh17')]")
    # Локатор для анимации (гифки) в модальном окне

    COOKING_TEXT = (By.XPATH, "//p[contains(text(), 'начали готовить')]")
    # Локатор для текста "Ваш заказ начали готовить"

    WAITING_TEXT = (By.XPATH, "//p[contains(text(), 'орбитальной станции')]")
    # Локатор для текста "Дождитесь готовности на орбитальной станции"

    MODAL_CLOSE_BUTTON = (By.XPATH,
                          "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    # Локатор для кнопки закрытия модального окна (крестик)