import pytest

from core.config import cfg
from core.driver import create_driver


@pytest.fixture(scope="session")  # одна конфигурация на все тесты
def config():
    return cfg


@pytest.fixture()  # новый браузер на каждый тест
def driver(config):
    drv = create_driver(config)
    yield drv
    drv.quit()
