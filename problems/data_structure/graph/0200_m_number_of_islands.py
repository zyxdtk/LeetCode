"""
难度: medium
标签: 深度优先搜索、广度优先搜索、并查集、矩阵

题目描述:
给你一个由 '1'（陆地）和 '0'（水）组成的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

示例:
输入: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出: 1
输入: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出: 3
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS解法
        时间复杂度: O(m*n)
        空间复杂度: O(m*n) 最坏情况下递归栈深度
        """
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(i+di, j+dj)
                
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
                    
        return count


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
            self.assertEqual(self.solution.numIslands(grid), 1)
            
        def test_case2(self):
            grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
            self.assertEqual(self.solution.numIslands(grid), 3)
            
    unittest.main()