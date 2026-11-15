from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
