from typing import Any
import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# ТЕСТЫ ДЛЯ filter_by_currency


def test_filter_by_currency_usd(sample_transactions: list[dict[str, Any]]) -> None:

    result = list(filter_by_currency(sample_transactions, "USD"))

    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268


def test_filter_by_currency_rub(sample_transactions: list[dict[str, Any]]) -> None:

    result = list(filter_by_currency(sample_transactions, "RUB"))

    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_filter_by_currency_empty_result(sample_transactions: list[dict[str, Any]]) -> None:

    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list() -> None:

    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


# ТЕСТЫ ДЛЯ transaction_descriptions


def test_transaction_descriptions(sample_transactions: list[dict[str, Any]]) -> None:

    result = list(transaction_descriptions(sample_transactions))

    assert len(result) == 3
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:

    result = list(transaction_descriptions([]))
    assert len(result) == 0


# ТЕСТЫ ДЛЯ card_number_generator


def test_card_number_generator_range() -> None:

    result = list(card_number_generator(1, 5))

    assert len(result) == 5
    assert result[0] == "0000 0000 0000 0001"
    assert result[-1] == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "start, stop, expected_count",
    [
        (1, 1, 1),
        (10, 12, 3),
        (9999999999999998, 9999999999999999, 2),
    ],
)
def test_card_number_generator_counts(
    start: int, stop: int, expected_count: int
) -> None:

    result = list(card_number_generator(start, stop))
    assert len(result) == expected_count
