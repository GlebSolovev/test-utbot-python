import math


def inc(x: int) -> int:
    return x + 1


def invert(b: bool) -> bool:
    return not b


def reverse(s: str) -> str:
    return s[::-1]


def capitalize(b: bytes) -> bytes:
    return b.capitalize()


def double_sqrt(x: float) -> float:
    return math.sqrt(math.sqrt(x))


def get_nan() -> float:
    return math.nan


def get_inf(s: int) -> float:
    return math.inf * s


def add_many_floats(x: float) -> float:
    for _ in range(1000):
        x += .1
    return x


def hello():
    print("hello")
