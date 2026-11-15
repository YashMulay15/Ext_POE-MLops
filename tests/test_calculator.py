import pytest
from app.calculator import add


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_add_mixed():
    assert add(-2, 5) == 3


def test_add_float():
    assert add(1.5, 2.5) == 4.0


@pytest.mark.parametrize("a,b,expected", [(0, 0, 0), (10, 20, 30), (100, -50, 50)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected