from abc import ABC, abstractmethod


class Base:
    def __init__(self, base_value: int):
        self.base_value = base_value
        self.value = base_value

    def say_hello(self) -> str:
        return "hello from Base: " + str(self.base_value)


class Derived(Base):
    def __init__(self, derived_value: int):
        super().__init__(derived_value - 1)
        self.derived_value = derived_value
        self.value = derived_value

    def say_hello(self) -> str:
        return "hello from Derived: " + str(self.derived_value)


def inc_value(base: Base) -> Base:
    base.value += 1
    base.say_hello()
    return base


def hello_derived(derived: Derived) -> str:
    return derived.say_hello()


def inc_derived_value(derived: Derived) -> Derived:
    derived.derived_value += 1
    derived.say_hello()
    return derived


class AbstractClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def abstract_get_value(self) -> int:
        raise NotImplementedError

    def to_int(self) -> int:
        return self.abstract_get_value()


class AbstractClassImpl(AbstractClass):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def abstract_get_value(self) -> int:
        return self.value


def id_and_print_abstract_class(abstract_class: AbstractClass) -> AbstractClass:
    print(abstract_class.to_int())
    return abstract_class


def id_and_print_abstract_class_impl(abstract_class_impl: AbstractClassImpl) -> AbstractClassImpl:
    print(abstract_class_impl.to_int())
    return abstract_class_impl
