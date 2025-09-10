import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage, Locator


class LoginModal(BasePage):
    """
    Компонент модального окна авторизации.
    Наследуемся от BasePage, чтобы использовать find/click/type и общий driver/base_url.
    """

    # --- ЛОКАТОРЫ  ---
    MODAL: Locator = (
        By.CSS_SELECTOR,
        "div[data-popup='login'].popups__item.active",
    )  # корневой контейнер модалки
    FIELD_LOGIN: Locator = (By.ID, "pop_up_username")  # input логина/email
    FIELD_PASSWORD: Locator = (By.ID, "pop_up_password")  # input пароля
    BTN_SUBMIT: Locator = (By.ID, "pop_up_button")  # кнопка «Войти»
    CLOSE_ICON: Locator = (By.CSS_SELECTOR, ".popups__close")  # крестик закрытия
    PASSWORD_TOGGLE: Locator = (By.CSS_SELECTOR, "img[alt='eye']")  # иконка показа/скрытия пароля
    # --- Раздел отправлений после входа (проверка успешной авторизации)
    LK_SHIPMENTS_HEADER: Locator = (
        By.XPATH,
        "//*[@id='departures_tab']/div",
    )  # проверяем что мы в отправлениях

    @allure.step("Дождаться открытия модального окна авторизации")
    def wait_opened(self, timeout: float = 10):
        self.find(self.MODAL, timeout)  # ждём появления корня модалки
        return self

    @allure.step("Ввести логин/email: {login}")
    def type_login(self, login: str):
        self.type(self.FIELD_LOGIN, login)
        return self

    @allure.step("Ввести пароль (скрыто)")
    def type_password(self, password: str):
        self.type(self.FIELD_PASSWORD, password)
        return self

    @allure.step("Нажать кнопку «Войти»")
    def submit(self):
        self.click(self.BTN_SUBMIT)
        return self

    @allure.step("Проверить, что пользователь попал в ЛК, раздел 'Отправления'")
    def should_be_shipments_open(self, timeout: float = 10):
        self.find(self.LK_SHIPMENTS_HEADER, timeout)  # ждём название аккаунта
        return self
