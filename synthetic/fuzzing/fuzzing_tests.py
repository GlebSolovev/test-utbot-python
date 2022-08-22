def check_constants_if_cases(x: int) -> str:
    if x == 5:
        return "5"
    elif x > 10:
        return "> 10"
    elif x < -5:
        return "-5"
    else:
        return "default"


def check_complicated_constants(x: int = 5) -> str:
    if x == 5:
        return "default param 5"

    ten, neg_ten = 10, -10
    if x > ten:
        return "> 10"
    if x < neg_ten:
        return "< -10"

    two_str = "2"
    if str(x) == two_str:
        return "2"

    seven_raw_str = """7"""
    if str(x) == seven_raw_str:
        return "7"

    fours_list = [4, -4]
    if x in fours_list:
        return "4 or -4"


def check_complex_constants(x: complex) -> str:
    if x > complex(5, 5):
        return "> 5 + 5i"
    return "<= 5 + 5i"


def check_constants_in_called_function(x: int) -> str:
    return check_constants_if_cases(x)
