"""
难度: medium
标签: 数组、矩阵、哈希表

题目描述:
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例:
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 使用第一行和第一列作为标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第一行和第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
            expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
            self.solution.setZeroes(matrix)
            self.assertEqual(matrix, expected)

        def test_case2(self):
            matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
            expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
            self.solution.setZeroes(matrix)
            self.assertEqual(matrix, expected)

        def test_case3(self):
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            self.solution.setZeroes(matrix)
            self.assertEqual(matrix, expected)

    unittest.main()
