"""
难度: medium
标签: 数组、动态规划

题目描述:
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。

示例:
输入: [1,2,3,1]
输出: 4
解释: 偷窃第1和第3间房屋 (1 + 3 = 4)
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃第1、3和5间房屋 (2 + 9 + 1 = 12)
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        prev_max = curr_max = 0
        for num in nums:
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        return curr_max


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,2,3,1]
            self.assertEqual(self.solution.rob(nums), 4)
            
        def test_case2(self):
            nums = [2,7,9,3,1]
            self.assertEqual(self.solution.rob(nums), 12)
            
    unittest.main()