import one


def test_add():
    assert one.add(1, 4) == 5
    assert one.add(-1, 4) == 3
    assert one.add(0, 5) == 5


def test_subtract():
    assert one.subtract(1, 4) == -3
    assert one.subtract(9, 0) == 9


def test_multiply():
    assert one.multiply(4, 5) == 20
    assert one.multiply(4, 0) == 0


def test_divid():
    assert one.division(30, 5) == 6
