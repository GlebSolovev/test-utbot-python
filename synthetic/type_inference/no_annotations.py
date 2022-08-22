"""
Type inference tests: check how well UTBot-Python deals with that.
"""

import heapq

"""
Default functions suite without any annotations.
"""


def id_(x):
    return x


def compare_with_5(x):
    return x > 5


def add(x, y):
    return x + y


def add_with_one(x, y):
    return x + y + 1


def add_with_one_with_unused_param(x, y, unused):
    return x + y + 1


def append_exclamation_mark(s):
    return s + "!"


def compare_with_hello(s):
    if s > "hello":
        return "> hello"
    else:
        return "< hello"


def append_two_ints(l):
    return l + [1, -1]


def append_ints_and_chars(l):
    return l + [1, -1] + list("ab")


def compare_with_list_len(x):
    l = [1, 2]
    if x > len(l):
        return "> 2"
    return "<= 2"


def format_data_labels(dates):
    if all(x.hour == 0 and x.minute == 0 for x in dates):
        return [x.strftime('%Y-%m-%d') for x in dates]
    else:
        return [x.strftime('%H:%M') for x in dates]


def typed_inc(x: int) -> int:
    return x + 1


def call_typed_inc(x):
    return typed_inc(x)


class ClassWithIntField:
    def __init__(self, int_field_value):
        self.int_field = int_field_value


class ClassWithAnnotatedIntField:
    def __init__(self, int_field: int):
        self.int_field = int_field


def inc_int_field(c):
    c.int_field += 1
    return c.int_field


class ClassWithUniquelyNamedMethod:
    def __init__(self, x: int):
        self.x = x

    def get_x_12345(self):
        return self.x


def call_uniquely_named_method(c):
    return c.get_x_12345()


def call_heapify(ints):
    return heapq.heapify(ints)


def concatenate_args(*args):
    return "+".join(args)


def concatenate_args_and_kwargs(*args, **kwargs):
    return "+".join(args) + ";" + "?".join(kwargs.values())


def raise_exception(exc):
    raise exc
