"""
难度: easy
标签: 数组、二分查找

题目描述:
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

示例:
输入: nums = [1,3,5,6], target = 5
输出: 2
输入: nums = [1,3,5,6], target = 2
输出: 1
输入: nums = [1,3,5,6], target = 7
输出: 4
"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分查找实现
        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,3,5,6]
            self.assertEqual(self.solution.searchInsert(nums, 5), 2)
            
        def test_case2(self):
            nums = [1,3,5,6]
            self.assertEqual(self.solution.searchInsert(nums, 2), 1)
            
        def test_case3(self):
            nums = [1,3,5,6]
            self.assertEqual(self.solution.searchInsert(nums, 7), 4)
            
    unittest.main()