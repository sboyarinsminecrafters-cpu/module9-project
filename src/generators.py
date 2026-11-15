from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте с помощью генератора.
    """
    return filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """
    Выводит описание транзакции с помощью генератора
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Создает (или генерирует) 16-тизначный номер карты с помощью итератора
    """

    def format_card(number: int) -> str:
        full_sequence = str(number).zfill(16)
        return f"{full_sequence[0:4]} {full_sequence[4:8]} {full_sequence[8:12]} {full_sequence[12:16]}"

    return map(format_card, range(start, stop + 1))
