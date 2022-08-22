from typing import List, Union, Dict, Tuple

my_int = int


def inc(x: my_int) -> my_int:
    return x


def add(x: my_int, y: int) -> int:
    return x + y


int_list = List[int]


def sort(l: int_list) -> int_list:
    l.sort()
    return l


strange = Union[List[Dict[Tuple[int, str]]]]


def handle_strange(s: strange):
    for l in s:
        return "".join(l.values())
