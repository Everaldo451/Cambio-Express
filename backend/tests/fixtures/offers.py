import pytest

@pytest.fixture
def offer_data():
    return {
        'code': 'USD',
        'min_value': '100.00',
        'index_variable': 'SELIC',
        'percent': '95.55'
    }