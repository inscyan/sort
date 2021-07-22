""" 选择排序（升序）
特点：
1、不断地选择剩余元素之中的最小者
2、内循环：比较当前元素与目前已知的最小元素，更新最小元素索引。外循环：交换元素
3、运行时间与输入无关：甭管数组是有序无序或是元素全部相等
4、数据移动是最少的：交换次数和数组的大小呈线性关系
5、不是稳定排序：https://www.zhihu.com/question/296361696/answer/1052158768
6、属于原地排序
力扣：`912. 排序数组`(超出时间限制)
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used


class Solution:
    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length):
            # 将 nums[i] 与 nums[i+1, ..., length-1] 中最小的元素进行交换
            min_idx = i  # 初始化最小元素索引
            for j in range(i + 1, length):
                if nums[j] < nums[min_idx]:
                    min_idx = j  # 更新最小元素索引
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]  # 交换元素

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
