"""
难度: medium
标签: 数组、二分查找、动态规划

题目描述:
给定一个整数数组 nums，找到其中最长严格递增子序列的长度。

示例:
输入: nums = [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长递增子序列是 [2,3,7,101]，因此长度为4
输入: nums = [0,1,0,3,2,3]
输出: 4
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划解法
        时间复杂度: O(n^2)
        空间复杂度: O(n)
        """
        if not nums:
            return 0
            
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [10,9,2,5,3,7,101,18]
            self.assertEqual(self.solution.lengthOfLIS(nums), 4)
            
        def test_case2(self):
            nums = [0,1,0,3,2,3]
            self.assertEqual(self.solution.lengthOfLIS(nums), 4)
            
    unittest.main()