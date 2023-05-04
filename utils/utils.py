def binary_search(sequence, start, end, value):
    while start < end:
        mid = (start + end) >> 1
        if value > sequence[mid]:
            start = mid + 1
        else:
            end = mid

    if sequence[start] == value:
        return start

    return -1


def quick_sort(sequence, start, end, less):
    """
    Sorts given sequence in place. Sequence should contain elements with identical structure.
    :param sequence: sequence, which will be sorted in place!
    :param start: left pointer of sequence index
    :param end: right pointer of sequence index
    :param less: mini comparator function, which gives True in case first item is strictly less than second.
    :return: sequence (the same pointer, which was received).
    """
    i, j = start, end
    pivot = sequence[(i + j) >> 1]

    while i <= j:
        while less(sequence[i], pivot):
            i += 1

        while less(pivot, sequence[j]):
            j -= 1

        if i <= j:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            i += 1
            j -= 1

    if start < j:
        quick_sort(sequence, start, j, less)
    if i < end:
        quick_sort(sequence, i, end, less)

    return sequence
