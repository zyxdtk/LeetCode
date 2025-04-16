"""
难度: medium
标签: 数组、矩阵、模拟

题目描述:
给你一个 m 行 n 列的矩阵 matrix ，请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例:
输入: matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
输出: [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历上层
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # 从上到下遍历右列
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:  # 防止单行情况
                # 从右到左遍历下层
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:  # 防止单列情况
                # 从下到上遍历左列
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res

if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
        
        def test_case1(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            expected = [1,2,3,6,9,8,7,4,5]
            self.assertEqual(self.solution.spiralOrder(matrix), expected)
            
        def test_case2(self):
            matrix = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]
            ]
            expected = [1,2,3,4,8,12,11,10,9,5,6,7]
            self.assertEqual(self.solution.spiralOrder(matrix), expected)
            
        def test_case3(self):
            matrix = []
            self.assertEqual(self.solution.spiralOrder(matrix), [])
    
    unittest.main()