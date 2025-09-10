import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage, Locator


class HomePage(BasePage):
    # Локаторы
    LOGO: Locator = (By.XPATH, '//*[@id="landing-header-logo"]/img')  # логотип
    SEARCH_BUTTON: Locator = (By.ID, "calculationFind")  # кнопка поиска
    LK_BUTTON: Locator = (By.ID, "menu_login_button")  # кнопка «Личный кабинет» в шапке

    @allure.step("Открыть главную страницу")
    def open_home(self):
        """Открыть главную страницу."""
        return self.open("/")

    @allure.step("Открыть модальное окно авторизации через кнопку «Личный кабинет»")
    def open_login_modal(self):
        self.click(self.LK_BUTTON)
        return self  # можно сразу вернуть self для чейнинга
