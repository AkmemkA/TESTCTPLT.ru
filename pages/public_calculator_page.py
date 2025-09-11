import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage


class PublicCalculatorPage(BasePage):
    """Калькулятор на главной для НЕавторизованных пользователей."""

    # 1) Первый экран: города
    SENDER_CITY_INPUT = (By.CSS_SELECTOR, "#senderCity")
    RECEIVER_CITY_INPUT = (By.CSS_SELECTOR, "#receiverCity")
    NEXT_TO_CARGO_BTN = (By.CSS_SELECTOR, "[data-qa='to-cargo-step']")

    # 2) Второй экран: тип отправления и параметры груза
    SHIPMENT_TYPE_DOCS = (By.CSS_SELECTOR, "[data-qa='type-docs']")
    WEIGHT_INPUT = (By.CSS_SELECTOR, "[data-qa='public-weight']")
    FIND_BTN = (By.CSS_SELECTOR, "[data-qa='public-find']")

    # 3) Страница результатов (после сабмита открывается новая страница)
    RESULT_ITEM = (By.CSS_SELECTOR, "[data-qa='tariff-item']")

    @allure.step("Ввести города: {sender} → {receiver}")
    def set_cities(self, sender: str, receiver: str):
        self.type(self.SENDER_CITY_INPUT, sender)
        self.type(self.RECEIVER_CITY_INPUT, receiver)
        return self

    @allure.step("Перейти к параметрам груза")
    def go_to_cargo_step(self):
        self.click(self.NEXT_TO_CARGO_BTN)
        return self

    @allure.step("Выбрать 'Документы' и вес {weight} кг")
    def set_cargo(self, weight: float):
        self.click(self.SHIPMENT_TYPE_DOCS)
        self.type(self.WEIGHT_INPUT, str(weight))
        return self

    @allure.step("Найти предложения (переход на страницу результатов)")
    def submit(self):
        self.click(self.FIND_BTN)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_any_elements_located(self.RESULT_ITEM)
        )
        return self

    @allure.step("Должно быть ≥{count} предложений")
    def should_have_offers(self, count=10):
        items = self.driver.find_elements(*self.RESULT_ITEM)
        assert len(items) >= count, f"Ожидали ≥{count}, получили {len(items)}"
        return self
