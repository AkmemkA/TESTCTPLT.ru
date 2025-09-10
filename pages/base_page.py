import time
from typing import Tuple

from selenium.webdriver import Keys
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
        return self  # вернет self для чейнинга

    def find(self, locator: Locator, timeout: float = 10):
        """Дождаться появления элемента в DOM и вернуть его."""
        by, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_all(self, locator, timeout=10):
        """Дождаться появления всех элементов в DOM и вернуть их."""
        by, value = locator
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def click(self, locator: Locator, timeout: float = 10):
        """Клик по элементу, дождавшись кликабельности."""
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.click()

    def type(self, locator: Locator, text: str, timeout: float = 10, clear: bool = True):
        """
        :param locator: Локатор элемента
        :param text: Текст для ввода
        :param timeout: Таймаут ожидания
        :param clear: Очищать ли поле перед вводом
        """
        by, value = locator
        el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))
        el.click()
        if clear:
            el.send_keys(Keys.CONTROL + "a")  # Выделить всё
            el.send_keys(Keys.DELETE)  # Удалить
        # Посимвольный ввод для стабильности
        for char in str(text):
            el.send_keys(char)
            time.sleep(0.05)  # Небольшая пауза между символами
        # Триггерим события для React/Vue приложений
        el.send_keys(Keys.TAB)
        # Проверяем, что текст ввелся корректно
        actual_text = el.get_attribute("value")
        if actual_text != text:
            # Если текст не совпадает, пробуем еще раз
            el.clear()
            el.send_keys(text)
        return self
