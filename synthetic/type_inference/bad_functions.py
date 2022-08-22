import math


def mixed_int_and_list(x):
    a = math.pow(x, 2)
    b = x.upper()
    return a + b


def mixed_int_str_list_and_field(x):
    x = x + 1
    if (x + "!") > len(x + [1, 2]):  # type: ignore
        return "yes"
    return x.some_field
