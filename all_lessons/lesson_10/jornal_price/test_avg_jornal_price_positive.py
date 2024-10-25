import pytest

from all_lessons.functions_pytest import average_jornal_price, journal_dict


@pytest.mark.avg_jornal_price
def test_avg_jornal_price_more_10000_volume():
    result = average_jornal_price(journal_dict)
    assert result == 10.065

@pytest.mark.avg_jornal_price
def test_avg_jornal_price_all_volume_less_10000():
    journal_dict = [
        {'name': 'Space', 'volume': 2000, 'price': 12.45},
        {'name': 'SeaSide', 'volume': 5000, 'price': 10.45},
        {'name': 'Fortune', 'volume': 10000, 'price': 17.99},
        {'name': 'Vouge', 'volume': 2500, 'price': 7.68}
    ]
    result = average_jornal_price(journal_dict)
    assert result == 0