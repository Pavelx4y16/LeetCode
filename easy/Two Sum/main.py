from utils.utils import quick_sort, binary_search
from bisect import bisect_left


def get_sum_indexes_1(nums, target):
    sorted_nums = list(enumerate(nums))
    quick_sort(sorted_nums, key=lambda x: x[1])

    for i, item in enumerate(sorted_nums):
        found_index = binary_search(sorted_nums, target - item[1], start=i + 1, key=lambda x: x[1])
        if found_index != -1:
            return sorted([item[0], sorted_nums[found_index][0]])


def get_sum_indexes_2(nums, target):
    sorted_nums = sorted(list(enumerate(nums)), key=lambda x: x[1])

    for i, item in enumerate(sorted_nums):
        found_index = binary_search(sorted_nums, target - item[1], start=i + 1, key=lambda x: x[1])
        if found_index != -1:
            return sorted([item[0], sorted_nums[found_index][0]])


def get_sum_indexes_3(nums, target):
    sorted_nums_with_indexes = sorted(list(enumerate(nums)), key=lambda x: x[1])
    sorted_nums = [item[1] for item in sorted_nums_with_indexes]

    for i, item in enumerate(sorted_nums):
        search_value = target - item
        found_index = bisect_left(sorted_nums, search_value, i + 1)
        if found_index < len(sorted_nums) and sorted_nums[found_index] == search_value:
            return sorted([sorted_nums_with_indexes[i][0], sorted_nums_with_indexes[found_index][0]])


def get_sum_indexes(nums, target):
    class ComplexData:
        def __init__(self, nums: list):
            self.nums = sorted(list(enumerate(nums)), key=lambda x: x[1])

        def __getitem__(self, index):
            return self.nums[index][1]

        def get_index(self, index):
            return self.nums[index][0]

        def __len__(self):
            return len(self.nums)

    nums = ComplexData(nums)

    for i in range(len(nums)):
        search_value = target - nums[i]
        found_index = bisect_left(nums, search_value, i + 1)
        if found_index < len(nums) and nums[found_index] == search_value:
            return sorted([nums.get_index(i), nums.get_index(found_index)])
