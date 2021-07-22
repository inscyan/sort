""" 希尔排序（升序）
特点：
1、基于插入排序：交换不相邻的元素以对数组的局部进行排序，并最终用插入排序将局部有序的数组排序
2、使数组中任意间隔为h的元素都是有序的。这样的数组被称为h有序数组
3、在进行排序时，如果h很大，我们就能将元素移动到很远的地方，为实现更小的h有序创造方便
4、不是稳定排序
5、属于原地排序
力扣：`912. 排序数组`(通过)
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used


class Solution:
    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        h = 1
        while h < length // 3:
            h = 3 * h + 1

        while h >= 1:
            # 将数组变为h有序
            for i in range(h, length):
                # 将nums[i]插入到nums[i-h]、nums[i-2*h]、nums[i-3*h]...之中
                for j in range(i, 0, -h):
                    if nums[j] < nums[j - h]:
                        nums[j - h], nums[j] = nums[j], nums[j - h]
                    else:
                        break
            h = h // 3

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
