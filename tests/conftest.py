import pytest

@pytest.fixture
def sample_operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 11111111, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]

