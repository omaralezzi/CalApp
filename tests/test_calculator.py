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


def test_bitwise_and_or_xor():
    assert bit_and(6, 3) == 2
    assert bit_or(6, 3) == 7
    assert bit_xor(6, 3) == 5


def test_bitwise_shifts_and_not():
    assert lshift(1, 3) == 8
    assert rshift(8, 2) == 2
    # bit_not with 8 bits: ~0x0f == 0xf0 within 8 bits
    assert bit_not(0x0f, bits=8) == 0xf0


def test_bin_hex_conversion():
    assert to_bin(10) == "1010"
    assert to_hex(255) == "ff"
    assert from_bin("1010") == 10
    assert from_hex("ff") == 255


def test_negate():
    assert negate(5) == -5
    assert negate(-3) == 3


def test_percent():
    assert percent(50) == 0.5
    assert percent(1) == 0.01
