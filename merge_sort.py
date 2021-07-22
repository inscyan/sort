""" 归并排序（升序）
特点：
1、自顶向下：先递归地将数组分成两半分别排序，然后将两个有序的子数组归并成一个有序数组
2、自底向上：先归并那些微型数组，然后再成对归并得到的子数组。两两归并、四四归并、八八归并。。。
3、分类：自顶向下普通归并、自顶向下原地归并、自底向上普通归并、自底向上原地归并
4、普通归并和原地归并在于merge过程不同
5、主要缺点：所需的额外空间和N成正比（普通归并）
6、属于稳定排序
7、普通归并不属于原地排序，原地归并属于（自顶向下原地归并在不考虑递归栈的存储占用情况下）
力扣：`912. 排序数组`(通过)
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used, reverse
from insert_sort import general_insert_sort


class Solution:
    def merge(self, a, lo, mid, hi):
        """普通归并"""
        a1, a2 = a[lo:mid + 1], a[mid + 1:hi + 1]
        i, j = 0, 0

        for k in range(lo, hi + 1):
            if a1[i] <= a2[j]:
                a[k] = a1[i]
                i += 1
            else:
                a[k] = a2[j]
                j += 1
            if i == len(a1):
                for idx in range(j, len(a2)):
                    k += 1
                    a[k] = a2[idx]
                break
            if j == len(a2):
                for idx in range(i, len(a1)):
                    k += 1
                    a[k] = a1[idx]
                break

    def merge_inplace(self, a, lo, mid, hi):
        """原地归并
           参考：https://blog.csdn.net/ACdreamers/article/details/24244643
           (交换次数过多，感觉不是很高效)
        """
        i, j = lo, mid + 1
        while i < j and j <= hi:
            while i < j and a[i] <= a[j]:
                i += 1
            idx = j
            while j <= hi and a[j] < a[i]:  # 不能这么写：a[j] <= a[i]，这么写就不是稳定排序了
                j += 1
            reverse(a, i, idx - 1)
            reverse(a, idx, j - 1)
            reverse(a, i, j - 1)
            i += (j - idx)

    def t2b_merge_sort(self, a, lo, hi):
        """自顶向下"""
        # if hi <= lo:
        #     return

        if hi - lo <= 15:
            general_insert_sort(a, lo, hi)
            return

        # 分
        mid = lo + (hi - lo) // 2  # `(hi + lo) // 2` 这种写法中的 `hi + lo` 可能会造成溢出
        self.t2b_merge_sort(a, lo, mid)  # 将左边排序
        self.t2b_merge_sort(a, mid + 1, hi)  # 将右边排序

        # 治
        if a[mid] > a[mid + 1]:
            self.merge(a, lo, mid, hi)  # 归并结果
            # self.merge_inplace(a, lo, mid, hi)  # 归并结果

    def b2t_merge_sort(self, a, length):
        """自底向上"""
        sz = 1  # 子数组初始大小
        while sz < length:
            lo = 0  # 左边子数组的低位索引
            # 对 a[lo, ..., lo + sz - 1] 和 a[lo + sz, ..., lo + sz + sz - 1] 进行归并
            while lo < length - sz:  # 对单个数组进行 merge 操作没有意义，所以需要 lo + sz < length
                if a[lo + sz - 1] > a[lo + sz]:
                    self.merge(a, lo, lo + sz - 1, min(lo + sz + sz - 1, length - 1))
                    # self.merge_inplace(a, lo, lo + sz - 1, min(lo + sz + sz - 1, length - 1))
                lo += sz + sz
            sz += sz

    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        self.t2b_merge_sort(nums, 0, length - 1)
        # self.b2t_merge_sort(nums, length)

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
