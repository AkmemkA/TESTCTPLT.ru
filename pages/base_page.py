from typing import Tuple

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import (
    WebDriverWait,  # явные ожидания когда необходимы
)

Locator = Tuple[str, str]  # (By, "selector")


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver  # ссылка на WebDriver
        self.base_url = base_url  # базовый URL стенда

    @allure.step("Открыть страницу: {path}")  # ← шаг в отчёте
    def open(self, path: str = "/"):
        """Открыть страницу по относительному пути."""
        self.driver.get(self.base_url + path)  # переход по URL
        return self  # вернет self для чейнинга

    @allure.step("Найти элемент: {locator}")
    def find(self, locator: Locator, timeout: float = 10):
        """Дождаться появления элемента в DOM и вернуть его."""
        by, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator: Locator, timeout: float = 10):
        """Клик по элементу, дождавшись кликабельности."""
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def type(self, locator: Locator, text: str, timeout: float = 10):
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.clear()
        el.send_keys(text)
