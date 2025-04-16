"""
难度: medium
标签: 广度优先搜索、数组、矩阵

题目描述:
在给定的网格中，每个单元格可以有以下三个值之一：
0 表示空单元格；
1 表示新鲜橘子；
2 表示腐烂的橘子。
每分钟，任何与腐烂的橘子相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例:
输入: grid = [[2,1,1],[1,1,0],[0,1,1]]
输出: 4
输入: grid = [[2,1,1],[0,1,1],[1,0,1]]
输出: -1
"""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS解法
        时间复杂度: O(m*n)
        空间复杂度: O(m*n)
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        minutes = 0
        
        # 初始化队列和新鲜橘子计数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        # 如果没有新鲜橘子，直接返回0
        if fresh == 0:
            return 0
            
        # BFS处理
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            i, j, minutes = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj, minutes + 1))

        # 如果还有新鲜橘子，返回-1
        if fresh > 0:
            return -1

        return minutes

if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            grid = [[2,1,1],[1,1,0],[0,1,1]]
            self.assertEqual(self.solution.orangesRotting(grid), 4) 
        
        def test_case2(self):
            grid = [[2,1,1],[0,1,1],[1,0,1]]
            self.assertEqual(self.solution.orangesRotting(grid), -1)
    
    unittest.main()    