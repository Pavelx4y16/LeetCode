from random import randrange
from utils import quick_sort, binary_search


def test_quick_sort():
    # test with random numbers
    n = 100
    unsorted = [randrange(1_000_000_000) for _ in range(n)]

    expected = sorted(unsorted)
    actual = quick_sort(unsorted, 0, len(unsorted) - 1, lambda first, second: first < second)

    assert actual == expected

    # test list with indexes
    n = 100
    unsorted = [(randrange(1_000_000_000), i) for i in range(n)]

    expected = sorted(unsorted)
    actual = quick_sort(unsorted, 0, len(unsorted) - 1, lambda first, second: first[0] < second[0])

    assert actual == expected


def test_binary_search():
    sorted_list = [1, 1, 2, 5, 7, 9, 24, 24]

    search_values = [5, 3333, 1, 24]
    expected_values = [3, -1, 0, 6]
    actual_values = [binary_search(sorted_list, 0, len(sorted_list) - 1, value) for value in search_values]

    assert actual_values == expected_values
