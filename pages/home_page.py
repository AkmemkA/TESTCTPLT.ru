from selenium.webdriver.common.by import By  # способы поиска

from .base_page import BasePage, Locator  # базовый класс и тип локатора


class HomePage(BasePage):
    # ↓↓↓ поставь реальные локаторы проекта
    LOGO: Locator = (By.CSS_SELECTOR, "[data-qa='logo']")  # логотип
    SEARCH_INPUT: Locator = (By.CSS_SELECTOR, "[data-qa='search']")  # поле поиска
    SEARCH_BUTTON: Locator = (By.CSS_SELECTOR, "[data-qa='go']")  # кнопка поиска

    def open_home(self):
        """Открыть главную страницу."""
        return self.open("/")

    def search(self, text: str):
        """Выполнить поиск."""
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)
        return self
