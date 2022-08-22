import math
from typing import IO, NoReturn


def div_by_zero(x: int) -> int:
    return x // 0


def assertion_fails(x: int) -> bool:
    false = x * 0 != 0
    assert false
    return false


def sqrt_neg(x: float) -> float:
    return math.sqrt(abs(x) * -1)


def div_int_by_str(x: int):
    return x / "hello"  # type: ignore


def open_non_existing_file(filename_suffix: str) -> IO:
    return open("test-utbot-python-non-existing-file-123456" + filename_suffix, "r")


def raise_exception(exc: Exception) -> NoReturn:
    raise exc


class MyException(Exception):
    pass


class MyExtendedException(Exception):
    def __init__(self, message: str, x: int):
        self.message = message
        self.x = x

    def __str__(self):
        return self.message + str(self.x)


class MyAssertionError(AssertionError):
    pass


def raise_custom_exception(x: int) -> NoReturn:
    if x > 0:
        raise MyExtendedException("> 0", x)
    if x < 0:
        raise MyException("< 0")
    raise AssertionError(x)
