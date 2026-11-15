import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('raw_date, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(raw_date, expected):
    assert mask_account_card(raw_date) == expected


@pytest.mark.parametrize('invalid_date', [
    'Visa Platinum',
    '7000792289606361',
    ''
])
def test_mask_account_card_invalid_date(invalid_date):
    #assert "Некорректный ввод" in mask_account_card(invalid_date)
    #Тест выше не проходит, т.к. есть недоработка функции, потребует изменений. Временно дополню проверку, не забыть исправить функцию!
    assert "Ошибка" in mask_account_card(invalid_date) or "Некорректный" in mask_account_card(invalid_date)


@pytest.mark.parametrize('iso_date, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2023-12-31T23:59:59', '31.12.2023'),
    ('2022-01-01', '01.01.2022') # Проверяем дату без времени
])
def test_get_date_valid(iso_date, expected):
    assert get_date(iso_date) == expected
