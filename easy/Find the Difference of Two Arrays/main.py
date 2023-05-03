def find_difference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    a1 = set(nums1)
    a2 = set(nums2)

    return [list(a1 - a2), list(a2 - a1)]
