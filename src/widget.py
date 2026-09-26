from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(raw_account_card: str) -> str:
    """Маскирует номер карты или счёта в зависимости от типа"""
    parts = raw_account_card.rsplit(" ", 1)
    name = parts[0]
    number = parts[1]

    if "счет" in name.lower():
        masked = get_mask_account(number)

    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"
