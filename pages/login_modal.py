import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage, Locator


class LoginModal(BasePage):
    """
    Компонент модального окна авторизации.
    Наследуемся от BasePage, чтобы использовать find/click/type и общий driver/base_url.
    """

    # --- ЛОКАТОРЫ  ---
    MODAL: Locator = (By.CSS_SELECTOR, "[data-qa='auth-modal']")  # корневой контейнер модалки
    FIELD_LOGIN: Locator = (By.CSS_SELECTOR, "[data-qa='auth-login']")  # input логина/email
    FIELD_PASSWORD: Locator = (By.CSS_SELECTOR, "[data-qa='auth-password']")  # input пароля
    BTN_SUBMIT: Locator = (By.CSS_SELECTOR, "[data-qa='auth-submit']")  # кнопка «Войти»
    CLOSE_ICON: Locator = (By.CSS_SELECTOR, "[data-qa='auth-close']")  # крестик закрытия (опц.)

    # --- ЛК после входа (проверка успешной авторизации) ---
    # например, заголовок раздела «Отправления»:
    LK_SHIPMENTS_HEADER: Locator = (By.CSS_SELECTOR, "[data-qa='lk-shipments-title']")

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

    @allure.step("Проверить, что пользователь попал в ЛК, раздел «Отправления»")
    def should_be_in_shipments(self, timeout: float = 10):
        self.find(self.LK_SHIPMENTS_HEADER, timeout)  # ждём заголовок раздела
        return self
