# QA Autotests (UI + PyTest + Selenium, macOS)

## Быстрый старт
1) Скопируйте `.env.example` → `.env` и задайте `BASE_URL`.
2) Активируйте окружение: `source .venv/bin/activate`
3) Запуск смоков: `pytest -m smoke`

## Allure отчёты
- Результаты: `allure-results/`
- Просмотр локально: `allure serve allure-results`

## Структура
- `core/` — конфиг и драйвер
- `pages/` — Page Object
- `tests/` — тесты (смоки в `tests/smoke`)
