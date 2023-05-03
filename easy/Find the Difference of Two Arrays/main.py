from array import array


def find_difference_1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    a1 = set(nums1)
    a2 = set(nums2)

    return [list(a1 - a2), list(a2 - a1)]


def find_difference(nums1, nums2):
    """
    This solution is worse than previous.
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    from array import array
    SHIFT = 1000

    a1 = array("b", [0] * 2001)
    a2 = array("b", [0] * 2001)

    res1 = []
    res2 = []

    for x in nums1:
        a1[x+SHIFT] = 1

    for x in nums2:
        a2[x+SHIFT] = 1

    for i, x in enumerate(a1):
        if x and not a2[i]:
            res1.append(i - SHIFT)

    for i, x in enumerate(a2):
        if x and not a1[i]:
            res2.append(i - SHIFT)

    return [res1, res2]
