# Проект: Виджет банковских операций

## Цель проекта
Дать пользователю возможность видеть данные банковских операций:
- Номер карты или счета
- Дату проведения операции
- Получать список операций и т.д.

## Установка
1. Клонируйте репозиторий:
   `git clone git@github.com:sboyarinsminecrafters-cpu/module9-project.git`
2. Установите Poetry (если еще не установлен).
3. Перейдите в папку проекта и выполните команду:
   `poetry install --with lint`

## Использование

### Маскировка карт и счетов
Функция `get_mask_card_number` маскирует номер карты.
Функция `get_mask_account` маскирует номер счета.
Функция `mask_account_card` сама определяет, карта это или счет, и применяет нужную маскировку.

**Пример:**
```python
from src.widget import mask_account_card

print(mask_account_card('Visa Platinum 7000792289606361'))
# Вывод: Visa Platinum 7000 79** **** 6361

print(mask_account_card('Счет 73654108430135874305'))
# Вывод: Счет **4305
```


### Форматирование даты
Функция `get_date` преобразует дату из формата `ISO` в формат `ДД.ММ.ГГГГ.`

**Пример:**
```python
from src.widget import get_date

print(get_date('2024-03-11T02:26:18.671407'))
# Вывод: 11.03.2024 
```

### Обработка данных (фильтрация и сортировка)
Функция `filter_by_state` фильтрует операции по статусу (по умолчанию 'EXECUTED').
Функция `sort_by_date` сортирует операции по дате (по умолчанию по убыванию).

**Пример:**
```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 2, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(filter_by_state(operations))
# Вывод: [{'id': 1, 'state': 'EXECUTED', ...}]
```

## Тестирование
Для запуска тестов используется библиотека `pytest`.
Чтобы запустить все тесты, выполните:
`poetry run pytest`

Для проверки покрытия кода тестами:
`poetry run pytest --cov=src`

Для генерации HTML-отчета о покрытии (сохраняется в папку `htmlcov`):
`poetry run pytest --cov=src --cov-report=html`