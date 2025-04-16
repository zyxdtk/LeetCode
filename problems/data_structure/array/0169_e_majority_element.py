"""
难度: easy
标签: 数组、哈希表、分治、计数、排序

题目描述:
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊n/2⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例:
输入: [3,2,3]
输出: 3
输入: [2,2,1,1,1,2,2]
输出: 2
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore投票算法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [3,2,3]
            self.assertEqual(self.solution.majorityElement(nums), 3)
            
        def test_case2(self):
            nums = [2,2,1,1,1,2,2]
            self.assertEqual(self.solution.majorityElement(nums), 2)
            
    unittest.main()