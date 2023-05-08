from main import get_diagonals_sum
from utils.utils import _test


def test_standard_1():
    _test(func=get_diagonals_sum, expected=25, matrix=[[1, 2, 3],
                                                       [4, 5, 6],
                                                       [7, 8, 9]])


def test_standard_2():
    _test(func=get_diagonals_sum, expected=8, matrix=[[1] * 4,
                                                      [1] * 4,
                                                      [1] * 4,
                                                      [1] * 4])


def test_standard_3():
    _test(func=get_diagonals_sum, expected=5, matrix=[[5]])
