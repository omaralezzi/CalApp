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


def negate(a):
    """Return the value of a with its sign flipped."""
    return -a


def percent(a):
    """Convert a to a percentage (divide by 100)."""
    return a / 100
