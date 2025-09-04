from typing import Tuple

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

    def open(self, path: str = "/"):
        """Открыть страницу по относительному пути."""
        self.driver.get(self.base_url + path)  # переход по URL
        return self  # вернём self для чейнинга

    def find(self, locator: Locator, timeout: float = 10):
        """Дождаться появления элемента в DOM и вернуть его."""
        by, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, locator: Locator, timeout: float = 10):
        """Клик по элементу, дождавшись кликабельности."""
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.click()

    def type(self, locator: Locator, text: str, timeout: float = 10):
        """Ввести текст в поле."""
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.clear()
        el.send_keys(text)
