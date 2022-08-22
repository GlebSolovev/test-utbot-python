import heapq
from datetime import datetime
from typing import Any, List, Union, cast


def add_int(x, y: int):
    return x + y


def add_one(x):
    return x + 1


def add_one_with_default(x=0):
    return x + 1


def add_one_with_annotated_default(x: int = 0):
    return x + 1


def add_one_with_annotated_result(x) -> int:
    return x + 1


def add_default_one(x, y=1):
    return x + y


def add_annotated_default_one(x, y: int = 1):
    return x + y


def add_with_unused_param(x: int, y: int, unused):
    return x + y


def id_with_annotated_result(x) -> int:
    return x


def id_with_in_body_type(x) -> int:
    y: int
    y = x
    return y


def id_with_in_body_assert(x):
    assert x is int
    return x


def id_with_in_body_type_assert(x):
    assert type(x) is int
    return x


def id_with_in_body_cast(x):
    y = cast(x, int)
    return y


"""
Default functions suite without return types annotations.
"""


def id_(x: Any):
    return x


def compare_with_5(x: int):
    return x > 5


def add(x: int, y: int):
    return x + y


def append_exclamation_mark(s: str):
    return s + "!"


def append_two_ints_to_typing_list(l: List[int]):
    return l + [1, -1]


def append_two_ints_to_builtin_list(l: list):
    return l + [1, -1]


def append_ints_and_chars(l: List[Union[int, str]]):
    return l + [1, -1] + list("ab")


def format_data_labels(dates: List[datetime]):
    if all(x.hour == 0 and x.minute == 0 for x in dates):
        return [x.strftime('%Y-%m-%d') for x in dates]
    else:
        return [x.strftime('%H:%M') for x in dates]


class ClassWithIntField:
    def __init__(self, int_field_value):
        self.int_field = int_field_value


class ClassWithAnnotatedIntField:
    def __init__(self, int_field: int):
        self.int_field = int_field


def inc_int_field(c: ClassWithIntField):
    c.int_field += 1
    return c.int_field


def call_heapify(ints: List[int]):
    heapq.heapify(ints)
    return ints


def concatenate_args(*args: str):
    return "+".join(args)


def concatenate_args_and_kwargs(*args: str, **kwargs: str):
    return "+".join(args) + ";" + "?".join(kwargs.values())


def raise_exception(exc: Exception):
    raise exc
