import numbers
from enum import Enum
from typing import Text, AnyStr, Any, TextIO


def add(x: numbers.Real, y: numbers.Real) -> numbers.Real:
    return x + y


def capitalize_strings(x: Text) -> Text:
    return x.capitalize()


def concat_strings(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y


def id_(x: Any) -> Any:
    return x


def id_none(x: None) -> None:
    print(x)


def copy_to_new_file(file: TextIO) -> TextIO:
    new_file = open('new_file.txt', 'w')
    content = file.read()
    new_file.write(content)
    return new_file


def reverse(barr: bytearray) -> bytearray:
    barr.reverse()
    return barr


def copy(mv: memoryview) -> memoryview:
    bs = bytes(mv)
    return memoryview(bs)


def union(fs1: frozenset, fs2: frozenset) -> frozenset:
    return fs1.union(fs2)


def extend(rf: range) -> range:
    return range(rf.start, rf.stop + 1)


class Color(Enum):
    WHITE = 1
    BLACK = -1


def reverse_color(color: Color) -> Color:
    if color is Color.WHITE:
        return Color.BLACK
    return Color.WHITE
