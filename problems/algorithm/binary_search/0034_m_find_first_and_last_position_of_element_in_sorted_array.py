"""
难度: medium
标签: 数组、二分查找

题目描述:
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值，返回 [-1, -1]。

示例:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找解法
        时间复杂度: O(logn)
        空间复杂度: O(1)
        """
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_pos = find_left(nums, target)
        right_pos = find_right(nums, target)
        
        if left_pos <= right_pos and right_pos < len(nums) and nums[left_pos] == target and nums[right_pos] == target:
            return [left_pos, right_pos]
        return [-1, -1]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [5,7,7,8,8,10]
            self.assertEqual(self.solution.searchRange(nums, 8), [3,4])
            
        def test_case2(self):
            nums = [5,7,7,8,8,10]
            self.assertEqual(self.solution.searchRange(nums, 6), [-1,-1])
            
    unittest.main()