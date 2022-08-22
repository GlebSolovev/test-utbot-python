import sys
from typing import NoReturn


def fac(x: int) -> int:
    if x <= 0:
        return 1
    return x * fac(x - 1)


def infinite_print_if_neg(x: int) -> None:
    while x != 0:
        print(x)
        x -= 1


def while_true_print(x: int) -> None:
    while True:
        print(x)


def while_true_count(x: int) -> None:
    while True:
        x += 1


def exit_with(x: int) -> NoReturn:
    sys.exit(x)


def overflow(x: int) -> int:
    return overflow(x)
