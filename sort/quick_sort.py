""" 快速排序（升序）
特点：
1、采用了分治思想，当两个子数组都有序时整个数组也就自然有序了
2、兼备原地排序和NlogN时间复杂度
3、在切分不平衡时，程序可能会极为低效（潜在缺点）
4、不属于稳定排序
5、属于原地排序（只需要一个很小的辅助栈）
力扣：`912. 排序数组`(通过)
"""

import random
from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used
from insert_sort import general_insert_sort


class Solution:
    def partition2_book(self, nums, lo, hi):
        """两路切分，书上写法，切分后左子数组和右子数组更趋于等长，降低递归深度，更优"""
        random_idx = random.randint(lo, hi)  # 消除对输入的依赖
        nums[lo], nums[random_idx] = nums[random_idx], nums[lo]
        seg = nums[lo]  # 切分元素

        i, j = lo + 1, hi
        while True:
            while nums[i] < seg:  # 直到找到一个大于等于切分元素的元素
                i += 1
                if i >= hi:
                    break
            while nums[j] > seg:  # 直到找到一个小于等于切分元素的元素
                j -= 1
                if j <= lo:
                    break
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[lo], nums[j] = nums[j], nums[lo]  # 注意这里是和 j 交换

        return j

    def partition2(self, nums, lo, hi):
        """两路切分，性能不如 `partition2_book` """
        # [lo, i-1]<seg, [i]=seg, [i+1, hi]>=seg
        random_idx = random.randint(lo, hi)  # 消除对输入的依赖
        nums[lo], nums[random_idx] = nums[random_idx], nums[lo]
        seg = nums[lo]  # 切分元素

        i = lo
        for idx in range(lo + 1, hi + 1):
            if nums[idx] < seg:
                i = i + 1
                nums[i], nums[idx] = nums[idx], nums[i]
        nums[lo], nums[i] = nums[i], nums[lo]

        return i

    def partition3(self, nums, lo, hi):
        """三路切分，在数组中重复元素不多的情况下比标准的二分法多使用了很多次交换
           对于包含大量重复元素的数组，它将排序时间从线性对数级降低到了线性级别
        """
        # [lo...lt-1]<seg, [lt...i-1]=seg, [i...gt]未定, [gt+1...hi]>seg
        random_idx = random.randint(lo, hi)  # 消除对输入的依赖
        nums[lo], nums[random_idx] = nums[random_idx], nums[lo]
        seg = nums[lo]

        lt, i, gt = lo, lo + 1, hi
        while i <= gt:
            if nums[i] < seg:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt = lt + 1
                i = i + 1
            elif nums[i] > seg:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt = gt - 1
            else:
                i = i + 1

        return lt - 1, gt + 1

    def quick_sort(self, nums, lo, hi):
        # if lo >= hi:
        #     return

        if hi - lo <= 15:
            general_insert_sort(nums, lo, hi)
            return

        # 双路快排
        # i = self.partition2(nums, lo, hi)
        i = self.partition2_book(nums, lo, hi)
        self.quick_sort(nums, lo, i - 1)  # 将左半部分排序
        self.quick_sort(nums, i + 1, hi)  # 将右半部分排序

        # # 三路快排
        # i, j = self.partition3(nums, lo, hi)
        # self.quick_sort(nums, lo, i)  # 将左部分排序
        # self.quick_sort(nums, j, hi)  # 将右部分排序

    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)

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
