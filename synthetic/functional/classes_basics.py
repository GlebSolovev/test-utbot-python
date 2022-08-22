from dataclasses import dataclass
from typing import List


def id_and_print_object(obj: object) -> object:
    print(obj)
    return obj


class Dummy:
    pass


def propagate_dummy(d: Dummy) -> List[Dummy]:
    return [d, d]


class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


def to_info_str(user: User) -> str:
    return user.name + str(user.id)


def create_namesake(user: User) -> User:
    return User(user.name, user.id + 1)


class UsersDB:
    def __init__(self, users: List[User], admin: User, name: str):
        self.users = users
        self.admin = admin
        self.name = name
        self.__private_name = name + "<private>"


def clear_db(users_db: UsersDB) -> UsersDB:
    users_db.users.clear()
    return users_db


class ClassWithInnerClass:

    def __init__(self):
        self.x = 1
        self.inner = self.InnerClass()

    class InnerClass:
        def __init__(self):
            pass


def id_class_with_inner_class(c: ClassWithInnerClass) -> ClassWithInnerClass:
    return c


def id_inner_class(inner: ClassWithInnerClass.InnerClass) -> ClassWithInnerClass.InnerClass:
    return inner


class MyInt:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        return False


def add(x: MyInt, y: MyInt) -> MyInt:
    return MyInt(x.value + y.value)


class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next_node = next_node


def get_cycle(x: int) -> Node:
    n1 = Node(x)
    n2 = Node(x, n1)
    n1.next_node = n2
    return n1


@dataclass
class UserData:
    name: str
    id: int

    def to_user(self) -> User:
        return User(self.name, self.id)


def find_user(id_: int, user_datas: List[UserData]) -> UserData:
    for data in user_datas:
        if data.id == id_:
            return data
    return UserData("", 0)


class ClassWithProperty:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name + "!"

    def get_name(self):
        return self.__name + "?"

    name = property(get_name, set_name)


def alter_name(c: ClassWithProperty, new_name: str) -> ClassWithProperty:
    c.name = new_name
    return c
