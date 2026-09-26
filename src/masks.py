def get_mask_card_number(card_number: str) -> str:

    if len(card_number) != 16:
        return "Ошибка! Номер карты должен состоять из 16 цифр"

    first_slise = card_number[:4]
    second_slise = card_number[4:6]
    fourth_slise = card_number[12:16]
    return f"{first_slise} {second_slise}** **** {fourth_slise}"


def get_mask_account(account_number: str) -> str:
    if len(account_number) < 4:
        return "Ошибка! Номер счета должен содержать хотя бы 4 символа"

    mask_account = account_number[-4:]
    return f"**{mask_account}"
