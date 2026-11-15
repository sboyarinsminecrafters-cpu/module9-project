from typing import Any
import pytest


@pytest.fixture
def sample_operations():
    """Фикстура с тестовыми данными для операций."""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 11111111, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]


@pytest.fixture
def sample_transactions() -> list[dict[str, Any]]:
    """Фикстура с тестовыми транзакциями для генераторов."""
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        },
    ]
