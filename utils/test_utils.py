from random import randrange
from utils import quick_sort, binary_search


def test_quick_sort():
    # test with random numbers
    n = 100
    unsorted = [randrange(1_000_000_000) for _ in range(n)]

    expected = sorted(unsorted)
    # in place sort
    quick_sort(unsorted)

    assert unsorted == expected

    # test list with indexes
    n = 100
    unsorted = [(randrange(1_000_000_000), i) for i in range(n)]

    expected = sorted(unsorted)
    quick_sort(unsorted, key=lambda x: x[0])

    assert unsorted == expected


def test_binary_search():
    sorted_list = [1, 1, 2, 5, 7, 9, 24, 24]

    search_values = [5, 3333, 1, 24]
    expected_values = [3, -1, 0, 6]
    actual_values = [binary_search(sorted_list, value) for value in search_values]

    assert actual_values == expected_values

    # non trivial sequence
    sorted_list = [(1, 0), (1, 1), (2, 2), (5, 3), (7, 4), (9, 5), (24, 6), (24, 7)]
    actual_values = [binary_search(sorted_list, value, key=lambda item: item[0]) for value in search_values]

    assert actual_values == expected_values
