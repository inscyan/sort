""" 插入排序（升序）
特点：
1、当前索引左边的所有元素都是有序的，但它们的最终位置还不确定
2、对 已经有序或接近有序的数组、元素都相同的数组 进行排序，它的运行时间是接近线性的
3、属于稳定排序
4、属于原地排序
力扣：`912. 排序数组`(超出时间限制)
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used


class Solution:
    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        """对于部分有序和小规模的数组应该选择插入排序"""
        length = len(nums)

        # # 写法1
        # for i in range(1, length):  # 如果i从0开始，则 list(range(0, 0, -1)) 为 []，相等于内层不循环
        #     # 将nums[i]插入到nums[i-1]、nums[i-2]、nums[i-3]...之中
        #     for j in range(i, 0, -1):
        #         if nums[j] < nums[j - 1]:
        #             nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #         else:
        #             break

        # 更优写法，对应书上练习2.1.25
        for i in range(1, length):
            tmp = nums[i]
            j = i  # j保存元素tmp应该插入的位置
            while j > 0 and nums[j - 1] > tmp:
                nums[j] = nums[j - 1]  # 相较于`nums[j - 1], nums[j] = nums[j], nums[j - 1]`，访问数组的次数减半
                j -= 1
            nums[j] = tmp

        return nums


def general_insert_sort(arr, lo, hi):
    """
    更一般的插入排序，可指定数组排序范围
    :param arr:
    :param lo: 开始索引
    :param hi: 终止索引
    :return:
    """
    for i in range(lo + 1, hi + 1):
        tmp = arr[i]
        j = i
        while j > lo and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp


if __name__ == '__main__':
    solution = Solution()

    arr = generate_partially_ordered_arr()
    print('partially ordered:')
    arr_sort = solution.sortArray(arr)
    print('is sort:', all([arr_sort[i] <= arr_sort[i + 1] for i in range(len(arr_sort) - 1)]))
    # general_insert_sort(arr, 0, len(arr) - 1)
    # print('is sort:', all([arr[i] <= arr[i + 1] for i in range(len(arr) - 1)]))
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
