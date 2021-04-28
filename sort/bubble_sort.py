""" 冒泡排序（升序）
特点：
1、重复地走访要排序的数列，依次比较两个相邻的元素，如果顺序错误就把它们交换过来
2、属于稳定排序
3、属于原地排序
力扣：`912. 排序数组`(超出时间限制)
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used


class Solution:
    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length):
            swap_count = 0  # 交换次数
            for j in range(length - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap_count += 1
            if swap_count == 0:  # 已经有序
                break

        return nums


if __name__ == '__main__':
    solution = Solution()

    arr = generate_partially_ordered_arr()
    print('partially ordered:')
    arr_sort = solution.sortArray(arr)
    print('is sort:', all([arr_sort[i] <= arr_sort[i + 1] for i in range(len(arr_sort) - 1)]))
    print()

    arr = generate_lot_repeat_arr()
    print('lot repeat:')
    arr_sort = solution.sortArray(arr)
    print('is sort:', all([arr_sort[i] <= arr_sort[i + 1] for i in range(len(arr_sort) - 1)]))
    print()

    arr = generate_random_arr()
    print('random:')
    arr_sort = solution.sortArray(arr)
    print('is sort:', all([arr_sort[i] <= arr_sort[i + 1] for i in range(len(arr_sort) - 1)]))
