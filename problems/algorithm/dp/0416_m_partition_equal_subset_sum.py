"""
难度: medium
标签: 数组、动态规划

题目描述:
给定一个只包含正整数的非空数组，判断该数组是否可以被分割成两个子集，使得两个子集的和相等。

示例:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11]
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个和相等的子集
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        动态规划解法
        时间复杂度: O(n*sum)
        空间复杂度: O(sum)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
            
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[target]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1, 5, 11, 5]
            self.assertTrue(self.solution.canPartition(nums))
            
        def test_case2(self):
            nums = [1, 2, 3, 5]
            self.assertFalse(self.solution.canPartition(nums))
            
    unittest.main()