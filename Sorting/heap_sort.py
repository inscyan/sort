""" 堆排序（升序）
特点：
1、二叉堆：堆有序的完全二叉树，可用数组层级存储
2.1、根节点在索引0：k 的父节点的索引为 (k - 1) // 2，它的两个子节点的索引分别为 2k+1 和 2k+2
2.2、根节点在索引1：k 的父节点的索引为 k // 2，它的两个子节点的索引分别为 2k 和 2k+1
3、能实现对数级别的 插入元素(上浮) 和 删除最大元素(下沉)
4、堆排序：唯一能够同时最优地利用空间和时间的方法，当空间十分紧张的时候很流行
5、不属于稳定排序
6、属于原地排序
力扣：`912. 排序数组`(通过)
python heapq 用法：https://docs.python.org/zh-cn/3/library/heapq.html
"""

from typing import List

from utils import generate_partially_ordered_arr, generate_lot_repeat_arr, generate_random_arr, time_used


class Solution:
    def swim(self, a, i):
        """上浮(最大堆)
        i: 子节点索引
        """
        while i > 0 and a[(i - 1) // 2] < a[i]:
            a[(i - 1) // 2], a[i] = a[i], a[(i - 1) // 2]
            i = (i - 1) // 2  # 更新子节点的索引i

    def sink(self, a, i, hi):
        """下沉(最大堆)
        i: 父节点索引
        """
        while 2 * i + 1 <= hi:
            j = 2 * i + 1  # j：两个子节点中最大值的初始索引
            if j < hi and a[j] < a[j + 1]:  # 如有必要更新j
                j += 1
            if a[i] >= a[j]:
                break
            a[i], a[j] = a[j], a[i]
            i = j

    @time_used()
    def sortArray(self, nums: List[int]) -> List[int]:
        hi = len(nums) - 1

        # 从右至左递归地建立起堆的秩序。底下没有节点的不用下沉，它们可看做只有一个节点的最大堆
        # (如果一个节点的两个子节点都已经是堆了，那么在该节点上调用sink()可以将它们变成一个堆)
        for i in range((hi - 1) // 2, -1, -1):
            self.sink(nums, i, hi)
        while hi > 0:
            nums[hi], nums[0] = nums[0], nums[hi]
            hi -= 1
            self.sink(nums, 0, hi)

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
