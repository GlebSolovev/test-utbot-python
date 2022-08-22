import array
import queue
from collections import namedtuple
from multiprocessing import Queue
from typing import List, Tuple, Dict, Set, NamedTuple, Deque, Optional, Union, Iterable, Callable, NoReturn, TypeVar, \
    Sequence


class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


def twice(l: List) -> List:
    return l + l


def append_int(l: List[int], x: int) -> List[int]:
    l.append(x)
    return l


def append_user(l: List[User], user: User) -> List[User]:
    l.append(user)
    return l


def append_to_matrix(m: List[List[float]], row: List[float]) -> List[List[float]]:
    m.append(row)
    return m


def reverse_isu_tup(tup: Tuple[int, str, User]) -> Tuple[User, str, int]:
    x, s, user = tup
    return user, s, x


def reverse_int_tup(ints: Tuple[int, ...]) -> Tuple[int, ...]:
    l = list(*ints)
    l.reverse()
    return tuple(l)


def remove_last_user_name(cache: Dict[id, str]) -> Dict[int, str]:
    cache.popitem()
    return cache


def remove_user(db: Dict[int, User], user_id: int) -> Dict[int, User]:
    db.pop(user_id)
    return db


def intersect(s1: Set[int], s2: Set[int]) -> Set[int]:
    return s1.intersection(s2)


Point = namedtuple('Point', ['x', 'y'])


def find_middle(p1: Point, p2: Point) -> Point:
    return Point((p1.x + p2.y) / 2, (p1.y + p2.y) / 2)


def inc_if_not_none(x: Optional[int]) -> Optional[int]:
    if x is None:
        return None
    return x + 1


def append_concatenated(strs: Union[str, List[str]]) -> Union[str, List[str]]:
    if isinstance(strs, str):
        return strs
    return [''.join(strs), *tuple(strs)]


def clone_named(named: Union[str, User]) -> Union[str, User]:
    if isinstance(named, str):
        return named
    return User(named.name, named.id + 1)


def put_int(q: queue.Queue[int], x: int) -> queue.Queue[int]:
    q.put(x)
    return q


def put_user(q: queue.Queue[User], user: User) -> queue.Queue[User]:
    q.put(user)
    return q


def put_processed_int(q: Queue[int], processed_int: int) -> Queue[int]:
    q.put(processed_int)
    return q


def pop_last_int(d: Deque[int]) -> Deque[int]:
    d.pop()
    return d


def pop_last_user(d: Deque[User]) -> Deque[User]:
    d.pop()
    return d


def reverse_ints_arr(arr: array.array[int]) -> array.array[int]:
    arr.reverse()
    return arr


def reverse_users_arr(arr: array.array[User]) -> array.array[User]:
    arr.reverse()
    return arr


def reverse_ints(ints: Iterable[int]) -> Iterable[int]:
    res = []
    for i in ints:
        res.append(i)
    res.reverse()
    return res


def handle_zero(handler: Callable[[int], int]) -> int:
    return handler(0)


def get_int_comparator(x: int) -> Callable[[int], bool]:
    return lambda y: y > x


def raise_error(message: str) -> NoReturn:
    raise ValueError(message)


T = TypeVar('T')


def first(seq: Sequence[T]) -> T:
    return seq.index(0)
