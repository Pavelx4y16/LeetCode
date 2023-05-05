from main import get_max_number


def _test(func, expected, **kwargs):
    assert func(**kwargs) == expected


def test_standard_1():
    _test(func=get_max_number, expected=3, s="abciiidef", k=3)


def test_standard_2():
    _test(func=get_max_number, expected=2, s="aeiou", k=2)


def test_standard_3():
    _test(func=get_max_number, expected=2, s="leetcode", k=3)
