"""
难度: medium
标签: 数组、分治、排序、堆(优先队列)、快速选择

题目描述:
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

示例:
输入: nums = [3,2,1,5,6,4], k = 2
输出: 5
输入: nums = [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        使用最小堆实现
        时间复杂度: O(n log k)
        空间复杂度: O(k)
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        """
        快速选择算法实现
        时间复杂度: 平均O(n), 最坏O(n^2)
        空间复杂度: O(1)
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 将基准值移到末尾
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # 将基准值移到最终位置
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
                
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        # 第k个最大元素相当于第n-k个最小元素
        return select(0, len(nums) - 1, len(nums) - k)


if __name__ == "__main__":
    import unittest
    from typing import List
    import random
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [3,2,1,5,6,4]
            k = 2
            self.assertEqual(self.solution.findKthLargest(nums, k), 5)
            
        def test_case2(self):
            nums = [3,2,3,1,2,4,5,5,6]
            k = 4
            self.assertEqual(self.solution.findKthLargest(nums, k), 4)
            
    unittest.main()