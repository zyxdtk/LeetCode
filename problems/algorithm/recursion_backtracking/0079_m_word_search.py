"""
难度: medium
标签: 数组、回溯算法、矩阵

题目描述:
给定一个 m x n 二维字符网格 board 和一个字符串单词 word。如果 word 存在于网格中，返回 true；否则，返回 false。

示例:
输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出: true
输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出: true
输入: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出: false
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        回溯算法实现
        时间复杂度: O(m*n*3^L) L为单词长度
        空间复杂度: O(L) 递归栈深度
        """
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                if backtrack(i+di, j+dj, k+1):
                    return True
            board[i][j] = temp
            return False
            
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCCED"
            self.assertTrue(self.solution.exist(board, word))
            
        def test_case2(self):
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "SEE"
            self.assertTrue(self.solution.exist(board, word))
            
        def test_case3(self):
            board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
            word = "ABCB"
            self.assertFalse(self.solution.exist(board, word))
            
    unittest.main()