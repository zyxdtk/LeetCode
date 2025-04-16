"""
难度: hard
标签: 数组、二分查找、分治算法

题目描述:
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

示例:
输入: nums1 = [1,3], nums2 = [2]
输出: 2.0
解释: 合并数组 = [1,2,3]，中位数 2
输入: nums1 = [1,2], nums2 = [3,4]
输出: 2.5
解释: 合并数组 = [1,2,3,4]，中位数 (2 + 3) / 2 = 2.5
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找解法
        时间复杂度: O(log(min(m,n)))
        空间复杂度: O(1)
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        while left < right:
            i = (left + right) // 2
            j = half_len - i
            if nums1[i] < nums2[j-1]:
                left = i + 1
            else:
                right = i

        i = left
        j = half_len - i
        max_of_left = max(nums1[i-1] if i > 0 else float('-inf'), nums2[j-1] if j > 0 else float('-inf'))
        
        if (m + n) % 2 == 1:
            return max_of_left
        
        max_of_right = min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))
        return (max_of_left + max_of_right) / 2
    
if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums1 = [1, 3]
            nums2 = [2]
            expected = 2.0
            self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

        def test_case2(self):
            nums1 = [1, 2]
            nums2 = [3, 4]
            expected = 2.5
            self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

        def test_case3(self):
            nums1 = [0, 0]
            nums2 = [0, 0]
            expected = 0.0
            self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

        def test_case4(self):
            nums1 = []
            nums2 = [1]
            expected = 1.0
            self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)
    
    unittest.main()
        