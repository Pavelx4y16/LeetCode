from utils.utils import quick_sort, binary_search


def get_sum_indexes(nums, target):
    sorted_nums = list(enumerate(nums))
    quick_sort(sorted_nums, key=lambda x: x[1])

    for i, item in enumerate(sorted_nums):
        found_index = binary_search(sorted_nums, target - item[1], start=i + 1, key=lambda x: x[1])
        if found_index != -1:
            return sorted([item[0], sorted_nums[found_index][0]])
