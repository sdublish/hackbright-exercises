"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the two inputs."""
    sum1 = 0
    for i in numbers:
        sum1 = sum1+i

    return sum1


def subtract(numbers):
    """Return the second number subtracted from the first."""

    dif = numbers[0]
    for i in numbers[1:]:
        dif = dif - i
    return dif


def multiply(numbers):
    """Multiply the two inputs together."""
    prod = 1
    for i in numbers:
        prod = prod*i
    return prod


def divide(numbers):

    """Divide the first input by the second, returning a floating point."""
    quot = numbers[0]
    for i in numbers[1:]:
        quot = quot / i
    return quot


def square(numbers):
    """Return the square of the input."""

    # Needs only one argument

    return numbers[0] ** 2


def cube(numbers):
    """Return the cube of the input."""

    # Needs only one argument

    return numbers[0] ** 3


def power(numbers):
    """Raise num1 to the power of num and return the value."""

    result = numbers[0]
    for i in numbers[1:]:
        result = result**i

    return result


def mod(numbers):
    """Return the remainder of num / num2."""
    result = numbers[0]
    for i in numbers[1:]:
        result = result % i
    return result
