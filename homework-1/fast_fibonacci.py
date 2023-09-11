from math import sqrt


def fast_fibonacci(n):
    return int((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5))
