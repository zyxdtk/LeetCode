"""
难度: easy
标签: 数组、动态规划

题目描述:
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

示例:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        动态规划解法
        时间复杂度: O(n^2)
        空间复杂度: O(n^2)
        """
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[-1]
            curr_row = [1]
            
            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            
            curr_row.append(1)
            triangle.append(curr_row)
            
        return triangle


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
            self.assertEqual(self.solution.generate(5), expected)
            
        def test_case2(self):
            self.assertEqual(self.solution.generate(0), [])
            
        def test_case3(self):
            self.assertEqual(self.solution.generate(1), [[1]])
            
    unittest.main()