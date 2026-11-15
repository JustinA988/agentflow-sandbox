import pytest

from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(1, 4) == 0.25


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
