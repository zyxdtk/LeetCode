"""
难度: medium
标签: 数组、动态规划

题目描述:
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是连续子数组
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        动态规划解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not nums:
            return 0
            
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
                
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            result = max(result, max_prod)
            
        return result


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [2,3,-2,4]
            self.assertEqual(self.solution.maxProduct(nums), 6)
            
        def test_case2(self):
            nums = [-2,0,-1]
            self.assertEqual(self.solution.maxProduct(nums), 0)
            
    unittest.main()