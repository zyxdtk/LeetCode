"""
难度: medium
标签: 数组、二分查找、矩阵

题目描述:
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
1. 每行中的整数从左到右按升序排列
2. 每行的第一个整数大于前一行的最后一个整数

示例:
输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出: true
输入: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出: false
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        二分查找实现
        时间复杂度: O(log(mn))
        空间复杂度: O(1)
        """
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            self.assertTrue(self.solution.searchMatrix(matrix, 3))
            
        def test_case2(self):
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            self.assertFalse(self.solution.searchMatrix(matrix, 13))
            
    unittest.main()