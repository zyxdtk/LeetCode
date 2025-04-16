"""
难度: medium
标签: 数组、二分查找

题目描述:
假设按照升序排列的数组在预先未知的某个点上进行了旋转。请找出其中最小的元素。

示例:
输入: nums = [3,4,5,1,2]
输出: 1
输入: nums = [4,5,6,7,0,1,2]
输出: 0
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        二分查找解法
        时间复杂度: O(logn)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [3,4,5,1,2]
            self.assertEqual(self.solution.findMin(nums), 1)
            
        def test_case2(self):
            nums = [4,5,6,7,0,1,2]
            self.assertEqual(self.solution.findMin(nums), 0)
            
    unittest.main()