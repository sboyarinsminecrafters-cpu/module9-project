import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_number, expected', [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210987654", "9876 54** **** 7654"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize('invalid_card', [
    '123',
    '12345678912345678900',
    ''
])
def test_get_mask_account(invalid_card):
    assert 'Ошибка!' in get_mask_account(invalid_card)



@pytest.mark.parametrize('accaunt, expected', [
    ("73654108430135874305", "**4305"),
    ("12345678", "**5678"),
])
def test_get_mask_account(accaunt, expected):
    assert get_mask_account(accaunt) == expected

def test_get_mask_account_invalid():
    assert 'Ошибка!' in get_mask_account("123")