from selenium.webdriver.common.by import By


class FeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ALL_TIME_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за все время:')]")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]")

    TOP_ORDER = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]/li[1]/a)[1]") # Верхний заказ в Ленте Заказов
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi") # Всплывающее окно с деталями заказа
    COMPOSITION_TEXT = (By.CSS_SELECTOR, "p.text.text_type_main-medium.mb-8") # Текст "Состав" в всплывающем окне

    ORDER_NUMBER_IN_MODAL = (By.CSS_SELECTOR, "p.text_type_digits-default")

    # Заказ в ленте по номеру (динамический - будет дополняться номером)
    ORDER_IN_FEED_BY_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#0')]")

    # Ссылка на заказ в ленте (для клика)
    ORDER_LINK_IN_FEED_BY_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(text(), '#0')]/ancestor::a")

    # Счетчик "Выполнено за все время"
    ALL_TIME_COMPLETED_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    # Счетчик "Выполнено за сегодня"
    TODAY_COMPLETED_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    # Номер заказа "В работе"
    ORDER_IN_PROGRESS_NUMBER = (
        By.CSS_SELECTOR,
        "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li.text_type_digits-default"
    )