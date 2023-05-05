def binary_search(sequence, value, start=0, end=None, key=lambda x: x):
    """
    Does binary search of 'value' in 'sequence' starting from 'start' position and ending at 'end' position.
    :param sequence: iterable
    :param start: if you want to find your value not from 0 position - pass this param
    :param end: if you want to find your value not until sequence end position - pass this param
    :param value: value, which you want to search
    :param key: if you want to pass not trivial sequences here, provide 'key' as lambda function, it will be applied to
                all elements of the sequence. By the default key == lambda x: x
    :return: integer number --- index of found item in sequence or -1
    """
    end = end or len(sequence) - 1

    while start < end:
        mid = (start + end) >> 1
        if value > key(sequence[mid]):
            start = mid + 1
        else:
            end = mid

    if key(sequence[start]) == value:
        return start

    return -1


def quick_sort(sequence, start=0, end=None, key=lambda x: x):
    """
    Sorts given sequence in place. Sequence should contain elements with identical structure.
    :param sequence: sequence, which will be sorted in place!
    :param start: left pointer of sequence index
    :param end: right pointer of sequence index
    :param key: if you want to pass not trivial sequences here, provide 'key' as lambda function, it will be applied to
                all elements of the sequence. By the default key == lambda x: x
    :return: sequence (the same pointer, which was received).
    """
    end = end or len(sequence) - 1

    i, j = start, end
    pivot = sequence[(i + j) >> 1]

    while i <= j:
        while key(sequence[i]) < key(pivot):
            i += 1

        while key(sequence[j]) > key(pivot):
            j -= 1

        if i <= j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            i += 1
            j -= 1

    if start < j:
        quick_sort(sequence, start, j, key)
    if i < end:
        quick_sort(sequence, i, end, key)


def _test(func, expected, **kwargs):
    actual = func(**kwargs)
    assert actual == expected
