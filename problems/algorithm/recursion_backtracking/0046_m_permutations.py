"""
难度: medium
标签: 数组、回溯

题目描述:
给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

示例:
输入: nums = [1,2,3]
输出: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法实现
        时间复杂度: O(n!)
        空间复杂度: O(n)
        """
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,2,3]
            expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
            self.assertCountEqual(self.solution.permute(nums), expected)
            
        def test_case2(self):
            nums = [0,1]
            expected = [[0,1],[1,0]]
            self.assertCountEqual(self.solution.permute(nums), expected)
            
    unittest.main()