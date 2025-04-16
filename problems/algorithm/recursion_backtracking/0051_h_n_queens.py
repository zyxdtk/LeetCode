"""
难度: hard
标签: 数组、回溯算法

题目描述:
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后放置的棋子方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        回溯算法实现
        时间复杂度: O(n!)
        空间复杂度: O(n)
        """
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                d1 = row - col
                d2 = row + col
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue
                board[row][col] = 'Q'
                backtrack(row+1, cols | {col}, diag1 | {d1}, diag2 | {d2})
                board[row][col] = '.'
                
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set())
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            n = 4
            expected = [
                [".Q..","...Q","Q...","..Q."],
                ["..Q.","Q...","...Q",".Q.."]
            ]
            self.assertCountEqual(self.solution.solveNQueens(n), expected)
            
    unittest.main()