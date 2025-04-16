"""
难度: medium
标签: 贪心算法、数组

题目描述:
给定一个非负整数数组 nums，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃次数是2。第一次从下标0跳到下标1，第二次从下标1跳到下标4。
输入: nums = [2,3,0,1,4]
输出: 2
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        贪心算法解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [2,3,1,1,4]
            self.assertEqual(self.solution.jump(nums), 2)
            
        def test_case2(self):
            nums = [2,3,0,1,4]
            self.assertEqual(self.solution.jump(nums), 2)
            
    unittest.main()