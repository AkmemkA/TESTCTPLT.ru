import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import (
    Options as FirefoxOptions,  # опции для Firefox на будущее
)


def create_driver(cfg):
    """
    Фабрика драйвера на основе настроек.
    """
    if cfg.browser.lower() == "chrome":  # выбран Chrome?
        options = ChromeOptions()  # создаём объект опций
        if cfg.headless:  # headless-режим?
            options.add_argument("--headless=new")  # новый headless у Chrome
        options.add_argument("--no-sandbox")  # устойчивость в CI/контейнерах
        options.add_argument("--disable-gpu")  # отключаем GPU тоже для CI и Docker
        driver = webdriver.Chrome(options=options)  # создаём Chrome WebDriver

    elif cfg.browser.lower() == "firefox":  # выбран Firefox?
        options = FirefoxOptions()  # опции Firefox
        if cfg.headless:
            options.add_argument("--headless")  # headless у Firefox
        driver = webdriver.Firefox(options=options)  # создаём Firefox WebDriver

    else:
        raise ValueError(f"Unsupported browser: {cfg.browser}")  # подстрахуемся

    driver.implicitly_wait(cfg.implicit_wait)  # неявное ожидание для всех find()

    # Получаем размеры экрана
    screen_width, screen_height = pyautogui.size()
    # Задаем размер окна (90% от экрана для удобства)
    window_width = int(screen_width * 0.95)
    window_height = int(screen_height * 0.95)
    driver.set_window_size(window_width, window_height)  # единый размер окна → меньше флейков

    # Вычисляем позицию для центрирования
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2
    # Устанавливаем позицию окна
    driver.set_window_position(position_x, position_y)
    return driver  # возвращаем готовый драйвер
