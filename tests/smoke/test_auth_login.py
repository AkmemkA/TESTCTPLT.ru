import time

import allure
import pytest

from pages.home_page import HomePage
from pages.login_modal import LoginModal


@allure.title(
    "Смок: Авторизация через «Личный кабинет» и переход в личный кабинет пользователя (203)"
)
@pytest.mark.smoke
def test_auth_login_opens_and_logs_in(driver, config):
    """
    Предусловия: тестовый пользователь существует (логин/пароль в .env).
    Шаги:
      1) Открываем главную
      2) Кликаем «Личный кабинет» — открывается модалка
      3) Заполняем логин и пароль, нажимаем «Войти»
      4) Проверяем, что оказались в ЛК → в правом верхнем углу аккаунт пользователя
    Ожидаемый результат: успешная авторизация, виден аккаунт пользователя.
    """
    # 1) Открыть главную
    home = HomePage(driver, config.base_url).open_home()

    # 2) Открыть модалку
    home.open_login_modal()
    modal = LoginModal(driver, config.base_url).wait_opened(timeout=config.explicit_wait)

    # 3) Ввести логин/пароль и отправить форму
    modal.type_login(config.auth_login).type_password(config.auth_password).submit()

    # 4) Проверить, что мы в личном кабинете
    modal.should_be_shipments_open(timeout=config.explicit_wait)
    time.sleep(5)

    # 5) Скриншот для отчёта
    allure.attach(
        driver.get_screenshot_as_png(),
        name="ЛК — залогиненный пользователь",
        attachment_type=allure.attachment_type.PNG,
    )
