from __future__ import annotations

from typing import List


def add(x: 'int', y: 'int') -> 'int':
    return x + y


def call_len_with_partially_quoted_annotation(x: List['int']) -> 'int':
    return len(x)


def call_len_with_fully_quoted_annotation(x: 'List[int]') -> 'int':
    return len(x)


class Dummy:
    def __init__(self, x: 'int'):
        self.x = x


def inc_dummy(d: Dummy) -> int:
    d.x += 1
    return d.x


class DummyWithMethodsToTest:
    def __init__(self, x: int):
        self.x = x

    def inc_by_with_future_annotation(self, other: DummyWithMethodsToTest) -> int:
        self.x += other.x
        return self.x

    def inc_by_with_quoted_annotation(self, other: 'DummyWithMethodsToTest') -> int:
        self.x += other.x
        return self.x


def inc_with_turned_off_mypy(x: int) -> int:  # type: ignore
    return x + 1
