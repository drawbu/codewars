def check_for_factor(base: int, factor: int) -> bool:
    return not bool(base % factor)


def test():
    assert check_for_factor(10, 2) == True
    assert check_for_factor(63, 7) == True
    assert check_for_factor(2450, 5) == True
    assert check_for_factor(24612, 3) == True
    assert check_for_factor(9, 2) == False
    assert check_for_factor(653, 7) == False
    assert check_for_factor(2453, 5) == False
    assert check_for_factor(24617, 3) == False