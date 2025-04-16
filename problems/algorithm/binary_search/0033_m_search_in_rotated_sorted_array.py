"""
难度: medium
标签: 数组、二分查找

题目描述:
给你一个旋转后的有序数组 nums 和一个目标值 target，如果 nums 中存在这个目标值，则返回它的索引，否则返回 -1。

示例:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找解法
        时间复杂度: O(logn)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                
            # 判断哪一部分是有序的
            if nums[left] <= nums[mid]:  # 左半部分有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [4,5,6,7,0,1,2]
            self.assertEqual(self.solution.search(nums, 0), 4)
            
        def test_case2(self):
            nums = [4,5,6,7,0,1,2]
            self.assertEqual(self.solution.search(nums, 3), -1)
            
    unittest.main()