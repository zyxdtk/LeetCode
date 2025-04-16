"""
难度: medium
标签: 动态规划、广度优先搜索、数组

题目描述:
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例:
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
输入: coins = [2], amount = 3
输出: -1
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        动态规划解法
        时间复杂度: O(n*amount)
        空间复杂度: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            coins = [1, 2, 5]
            amount = 11
            self.assertEqual(self.solution.coinChange(coins, amount), 3)
            
        def test_case2(self):
            coins = [2]
            amount = 3
            self.assertEqual(self.solution.coinChange(coins, amount), -1)
            
    unittest.main()