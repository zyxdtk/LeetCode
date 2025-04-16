"""
难度: medium
标签: 广度优先搜索、数学、动态规划

题目描述:
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例:
输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4
输入: n = 13
输出: 2
解释: 13 = 4 + 9
"""

import math
from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        """
        动态规划解法
        时间复杂度: O(n√n)
        空间复杂度: O(n)
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            self.assertEqual(self.solution.numSquares(12), 3)
            
        def test_case2(self):
            self.assertEqual(self.solution.numSquares(13), 2)
            
    unittest.main()