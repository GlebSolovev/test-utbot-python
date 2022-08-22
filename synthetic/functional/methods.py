class Utils:

    UTILS_NAME = "UTILS"

    def __init__(self, value: int, name: str):
        self.value = value
        self.name = name

    def build_named_string(self, s: str) -> str:
        return s + ", name: " + self.name

    def __abs__(self):
        if self.value != 0:
            return Utils(abs(self.value), self.name)
        raise ValueError("don't like zeros")

    @staticmethod
    def print_great_string(s: str):
        return s.capitalize()

    @classmethod
    def create_utils(cls, value: int):
        return Utils(value, cls.UTILS_NAME)
