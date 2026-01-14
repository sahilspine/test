import pytest


def test_simple():
    assert 1 + 1 == 2


def test_with_fixture(sample_data):
    assert sample_data["name"] == "test"
    assert sample_data["value"] == 42


def test_with_list_fixture(sample_list):
    assert len(sample_list) == 5
    assert sum(sample_list) == 15
