import allure
from selenium.webdriver.common.by import By  # способы поиска

from .base_page import BasePage, Locator  # базовый класс и тип локатора


class HomePage(BasePage):
    # ↓↓↓ поставь реальные локаторы проекта
    LOGO: Locator = (By.XPATH, '//*[@id="landing-header-logo"]/img')  # логотип
    # SEARCH_INPUT: Locator = (By.ID, "senderCity")  # поле поиска To_do
    SEARCH_BUTTON: Locator = (By.ID, "calculationFind")  # кнопка поиска
    LK_BUTTON: Locator = (By.ID, "menu_login_button")  # кнопка «Личный кабинет» в шапке

    @allure.step("Открыть главную страницу")
    def open_home(self):
        """Открыть главную страницу."""
        return self.open("/")

    @allure.step("Открыть модальное окно авторизации через кнопку «Личный кабинет»")
    def open_login_modal(self):
        self.click(self.LK_BUTTON)
        return self  # можно сразу вернуть self для чейнинга (не Татума)

    # To_do
    # @allure.step("")
    # def search(self, text: str):
    #     """Выполнить поиск."""
    #     self.type(self.SEARCH_INPUT, text)
    #     self.click(self.SEARCH_BUTTON)
    #     return self
