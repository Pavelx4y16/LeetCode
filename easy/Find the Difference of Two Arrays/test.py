from main import find_difference


def test():
    actuals = [
        find_difference([1, 2, 3], [2, 4, 6]),
        find_difference([1, 2, 3, 3], [1, 1, 2, 2])
    ]
    expected = [
        [[1, 3], [4, 6]],
        [[3], []]
    ]

    assert actuals == expected
