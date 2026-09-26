from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(raw_account_card: str) -> str:
    """Маскирует номер карты или счёта в зависимости от типа"""
    parts = raw_account_card.rsplit(" ", 1)

    if len(parts) != 2:
        return "Некорректный ввод"

    name, number = parts

    if "счет" in name.lower():
        masked = get_mask_account(number)

    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(raw_date: str) -> str:
    """Преобразует дату из ISO в формат ДД.ММ.ГГГГ."""
    date_time = datetime.fromisoformat(raw_date)
    return date_time.strftime("%d.%m.%Y")
