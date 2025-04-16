"""
难度: easy
标签: 数组、动态规划

题目描述:
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
如果你不能获取任何利润，返回 0。

示例:
输入: prices = [7,1,5,3,6,4]
输出: 5
解释: 在第2天买入(价格=1)，在第5天卖出(价格=6)，最大利润=6-1=5。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        一次遍历解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            prices = [7,1,5,3,6,4]
            self.assertEqual(self.solution.maxProfit(prices), 5)
            
        def test_case2(self):
            prices = [7,6,4,3,1]
            self.assertEqual(self.solution.maxProfit(prices), 0)
            
    unittest.main()