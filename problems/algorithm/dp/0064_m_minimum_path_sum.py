"""
难度: medium
标签: 数组、动态规划、矩阵

题目描述:
给定一个包含非负整数的 m x n 网格 grid，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

示例:
输入: grid = [[1,3,1],[1,5,1],[4,2,1]]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        动态规划解法
        时间复杂度: O(m*n)
        空间复杂度: O(n)
        """
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        
        # 初始化第一行
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        for i in range(1, m):
            # 更新第一列
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
                
        return dp[-1]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            grid = [[1,3,1],[1,5,1],[4,2,1]]
            self.assertEqual(self.solution.minPathSum(grid), 7)
            
        def test_case2(self):
            grid = [[1,2,3],[4,5,6]]
            self.assertEqual(self.solution.minPathSum(grid), 12)
            
    unittest.main()