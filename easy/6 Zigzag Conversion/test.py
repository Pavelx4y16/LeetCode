from main import convert
from utils.utils import _test


def test_standard_1():
    _test(func=convert, expected="PAHNAPLSIIGYIR", s="PAYPALISHIRING", n=3)


def test_standard_2():
    _test(func=convert, expected="PINALSIGYAHRPI", s="PAYPALISHIRING", n=4)


def test_standard_3():
    _test(func=convert, expected="A", s="A", n=1)


def test_wa_1():
    _test(func=convert, expected="ABC", s="ABC", n=1)


def test_te_1():
    _test(func=convert, expected="jswmnckidivxubrjspdplacmetkizbjktfzihjrltoknpdyhsdyfdblrdjcwsdqrjyjfgbak", s="jswmnckidivxubrjspdplacmetkizbjktfzihjrltoknpdyhsdyfdbrjwdryfbkagjjqscdl", n=63)