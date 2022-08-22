def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def compound_interest(principle, rate, time):
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    return CI


# Python Program to find sum of square of first
# n natural numbers. This program avoids
# overflow upto some extent for large value
# of n.y
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3


