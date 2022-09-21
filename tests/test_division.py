"""This is the starting test file"""


def test_division():
    """This always passes"""
    sum_of_numbers = 4 / 2
    assert sum_of_numbers == 2


def test_division_if_zero():
    try:
        sum_of_numbers_zero = 6 / 0
    except ZeroDivisionError:
        sum_of_numbers_zero = 0

    assert sum_of_numbers_zero == 0
