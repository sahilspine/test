import pytest


@pytest.fixture
def sample_data():
    return {"name": "test", "value": 42}


@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]
