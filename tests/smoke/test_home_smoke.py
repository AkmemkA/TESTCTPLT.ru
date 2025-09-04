import allure
import pytest

from pages.home_page import HomePage


@allure.title("Главная страница открывается")  # как тест будет называться в Allure
@pytest.mark.smoke  # пометка, что это смок-тест
def test_homepage_opens(driver, config):
    page = HomePage(driver, config.base_url)  # создаём страницу с базовым URL
    page.open_home()  # открываем главную
    # time.sleep(3)
    assert driver.current_url.startswith(
        config.base_url
    ), "Ожидали, что откроется главная страница стенда"
