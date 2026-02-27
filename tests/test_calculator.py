import pytest
import math

from calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 2) == 8


def test_divide():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_negate():
    assert negate(5) == -5
    assert negate(-3) == 3


def test_percent():
    assert percent(50) == 0.5
    assert percent(1) == 0.01


def test_scientific():
    # trig functions at known angles
    assert sin(0) == 0
    assert cos(0) == 1
    assert tan(0) == 0
    # log and exp
    assert log(1) == 0
    assert exp(1) == pytest.approx(math.e)
    # sqrt and pi
    assert sqrt(4) == 2
    assert pi() == pytest.approx(math.pi)


def test_negate():
    assert negate(5) == -5
    assert negate(-3) == 3


def test_percent():
    assert percent(50) == 0.5
    assert percent(1) == 0.01
