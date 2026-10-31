import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)
    assert len(result) == 3
    for item in result:
        assert item['state'] == 'EXECUTED'


@pytest.mark.parametrize('state, expected_count', [
    ('EXECUTED', 3),
    ('CANCELED', 1),
    ('PENDING', 0),
])
def test_filter_by_state_custom(sample_operations, state, expected_count):
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count


def test_sort_by_date_descending(sample_operations):
    result = sort_by_date(sample_operations)
    assert result[0]['date'] == '2019-07-03T18:35:29.512364'
    assert result[-1]['date'] == '2018-06-30T02:08:58.425572'


def test_sort_by_date_ascending(sample_operations):
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]['date'] == '2018-06-30T02:08:58.425572'
    assert result[-1]['date'] == '2019-07-03T18:35:29.512364'