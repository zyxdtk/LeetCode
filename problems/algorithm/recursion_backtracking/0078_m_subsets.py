"""
难度: medium
标签: 位运算、数组、回溯算法

题目描述:
给定一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集（幂集）。

示例:
输入: nums = [1,2,3]
输出: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法实现
        时间复杂度: O(n*2^n)
        空间复杂度: O(n)
        """
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        res = []
        backtrack(0, [])
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,2,3]
            expected = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
            self.assertCountEqual(self.solution.subsets(nums), expected)
            
        def test_case2(self):
            nums = [0]
            expected = [[],[0]]
            self.assertCountEqual(self.solution.subsets(nums), expected)
            
    unittest.main()