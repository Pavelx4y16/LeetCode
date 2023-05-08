from main import get_substring
from utils.utils import _test


def test_standard_1():
    _test(func=get_substring, expected=3, s="abcabcbb")


def test_standard_2():
    _test(func=get_substring, expected=1, s="bbbbb")


def test_standard_3():
    _test(func=get_substring, expected=3, s="pwwkew")
