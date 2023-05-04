from main import get_sum_indexes


def test_standard_1():
    nums = [2, 7, 11, 15]
    target = 9

    expected = [0, 1]
    actual = get_sum_indexes(nums, target)

    assert actual == expected


def test_standard_2():
    nums = [3, 2, 4]
    target = 6

    expected = [1, 2]
    actual = get_sum_indexes(nums, target)

    assert actual == expected


def test_standard_3():
    nums = [3, 3]
    target = 6

    expected = [0, 1]
    actual = get_sum_indexes(nums, target)

    assert actual == expected


def test_negative_numbers():
    nums = [-3, 3, 2, 7, 1]
    target = 0

    expected = [0, 1]
    actual = get_sum_indexes(nums, target)

    assert actual == expected
