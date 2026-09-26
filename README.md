# SauceDemo UI Tests

![UI tests](https://github.com/nuralinmadiyar-max/saucedemo-playwright-tests/actions/workflows/tests.yml/badge.svg)

UI-автотесты для демо-магазина [SauceDemo](https://www.saucedemo.com) на Python + Playwright + pytest с паттерном Page Object. Тесты автоматически запускаются в GitHub Actions при каждом коммите.

## Что покрыто

- **Логин:** успешный вход и негативные сценарии (пустые поля, пустой пароль, заблокированный пользователь, неверные данные).
- **Каталог:** количество товаров, сортировка по имени (A→Z, Z→A) и по цене (по возрастанию и убыванию).
- **Корзина:** добавление одного и двух товаров, счётчик на значке корзины.

## Стек

Python, Playwright, pytest, Page Object, GitHub Actions

## Структура

```
pages/          Page Object: локаторы и действия для каждой страницы
tests/          тесты
conftest.py     фикстуры: открытие страницы логина, вход в каталог
pytest.ini      настройки pytest и адрес сайта
.github/        запуск тестов в GitHub Actions
```

## Как запустить

```
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
playwright install chromium
pytest -v
```

Запуск с видимым браузером: `pytest --headed`