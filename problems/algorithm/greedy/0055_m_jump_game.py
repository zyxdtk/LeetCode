"""
难度: medium
标签: 贪心算法、数组

题目描述:
给定一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

示例:
输入: nums = [2,3,1,1,4]
输出: true
解释: 可以先跳1步到位置1，然后再跳3步到达最后一个位置
输入: nums = [3,2,1,0,4]
输出: false
解释: 无论如何都会到达位置3，但该位置的最大跳跃长度是0，所以永远不能到达最后一个位置
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        贪心算法解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [2,3,1,1,4]
            self.assertTrue(self.solution.canJump(nums))
            
        def test_case2(self):
            nums = [3,2,1,0,4]
            self.assertFalse(self.solution.canJump(nums))
            
    unittest.main()