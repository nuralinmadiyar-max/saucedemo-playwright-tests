# SauceDemo UI Tests

![UI tests](https://github.com/nuralinmadiyar-max/saucedemo-playwright-tests/actions/workflows/tests.yml/badge.svg)

UI-автотесты для демо-магазина [SauceDemo](https://www.saucedemo.com) на Python + Playwright + pytest с паттерном Page Object. Тесты автоматически запускаются в GitHub Actions при каждом коммите, после прогона публикуется Allure-отчёт.

**Allure-отчёт последнего прогона:** https://nuralinmadiyar-max.github.io/saucedemo-playwright-tests/

## Что покрыто

20 автотестов:

- **Логин:** успешный вход и негативные сценарии (пустые поля, пустой пароль, заблокированный пользователь, неверные данные).
- **Каталог:** количество товаров, сортировка по имени (A→Z, Z→A) и по цене (по возрастанию и убыванию).
- **Корзина:** добавление товаров и счётчик на значке, отображение товара в корзине, удаление, возврат в каталог.
- **Оформление заказа:** валидация обязательных полей, проверка расчёта суммы, налога и итога, полный сценарий покупки.

## Стек

Python, Playwright, pytest, Page Object, Allure, GitHub Actions, GitHub Pages

## Структура

```
pages/          Page Object: локаторы и действия для каждой страницы
tests/          тесты
conftest.py     общие фикстуры и скриншот в отчёт при падении теста
pytest.ini      настройки pytest и адрес сайта
.github/        запуск тестов в GitHub Actions и публикация Allure-отчёта
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
