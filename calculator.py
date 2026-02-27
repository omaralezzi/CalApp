"""Simple calculator module providing basic arithmetic operations."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def negate(a):
    """Return the value of a with its sign flipped."""
    return -a


def percent(a):
    """Convert a to a percentage (divide by 100)."""
    return a / 100

import math


def sin(a):
    """Return the sine of *a* (radians)."""
    return math.sin(a)


def cos(a):
    """Return the cosine of *a* (radians)."""
    return math.cos(a)


def tan(a):
    """Return the tangent of *a* (radians)."""
    return math.tan(a)


def log(a):
    """Return the natural logarithm of *a*."""
    return math.log(a)


def exp(a):
    """Return *e* raised to the power of *a*."""
    return math.exp(a)


def sqrt(a):
    """Return the square root of *a*."""
    return math.sqrt(a)


def pi():
    """Return the mathematical constant pi."""
    return math.pi

    # Programmer / bitwise helpers
    def bit_and(a, b):
        """Return bitwise AND of two integers."""
        return int(a) & int(b)

    def bit_or(a, b):
        """Return bitwise OR of two integers."""
        return int(a) | int(b)

    def bit_xor(a, b):
        """Return bitwise XOR of two integers."""
        return int(a) ^ int(b)

    def bit_not(a, bits=32):
        """Return bitwise NOT of an integer within given bit width."""
        a = int(a)
        mask = (1 << bits) - 1
        return (~a) & mask

    def lshift(a, n):
        """Left shift integer a by n bits."""
        return int(a) << int(n)

    def rshift(a, n):
        """Right shift integer a by n bits."""
        return int(a) >> int(n)

    def to_bin(a):
        """Return binary representation (without '0b')."""
        return bin(int(a))[2:]

    def to_hex(a):
        """Return hexadecimal representation (without '0x'), lowercase."""
        return hex(int(a))[2:]

    def from_bin(s):
        """Parse binary string to int."""
        return int(str(s), 2)

    def from_hex(s):
        """Parse hex string to int."""
        return int(str(s), 16)


def negate(a):
    """Return the value of a with its sign flipped."""
    return -a


def percent(a):
    """Convert a to a percentage (divide by 100)."""
    return a / 100
