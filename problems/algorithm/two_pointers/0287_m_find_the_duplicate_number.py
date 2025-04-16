"""
难度: medium
标签: 位运算、数组、双指针、二分查找

题目描述:
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例:
输入: nums = [1,3,4,2,2]
输出: 2
输入: nums = [3,1,3,4,2]
输出: 3
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        快慢指针解法（Floyd判圈算法）
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        slow = fast = 0
        # 第一阶段：寻找相遇点
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 第二阶段：寻找环的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,3,4,2,2]
            self.assertEqual(self.solution.findDuplicate(nums), 2)
            
        def test_case2(self):
            nums = [3,1,3,4,2]
            self.assertEqual(self.solution.findDuplicate(nums), 3)
            
    unittest.main()