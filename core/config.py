import os  # доступ к переменным окружения
from dataclasses import dataclass  # удобный способ описать объект настроек

from dotenv import load_dotenv  # загрузка переменных из .env

load_dotenv()  # подхватываем .env из корня проекта


@dataclass(frozen=True)  # frozen: настройки нельзя менять в рантайме
class Config:
    base_url: str = os.getenv("BASE_URL", "")  # адрес стенда для тестов
    browser: str = os.getenv("BROWSER", "chrome")  # chrome или firefox
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"  # включён ли headless
    implicit_wait: float = float(os.getenv("IMPLICIT_WAIT", "0"))  # неявное ожидание
    explicit_wait: float = float(os.getenv("EXPLICIT_WAIT", "10"))  # явное ожидание по умолчанию


cfg = Config()  # один общий объект конфигурации
