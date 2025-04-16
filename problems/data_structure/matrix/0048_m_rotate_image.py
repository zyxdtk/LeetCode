"""
难度: medium
标签: 数组、数学、矩阵

题目描述:
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例:
输入: matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
输出: [
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 先转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 再翻转每一行
        for i in range(n):
            for j in range(0, n//2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            self.solution.rotate(matrix)
            self.assertEqual(matrix, expected)

        def test_case2(self):
            matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
            expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
            self.solution.rotate(matrix)
            self.assertEqual(matrix, expected)

        def test_case3(self):
            matrix = [[1]]
            expected = [[1]]
            self.solution.rotate(matrix)
            self.assertEqual(matrix, expected)

    unittest.main()
