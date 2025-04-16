"""
难度: medium
标签: 数组、双指针

题目描述:
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

示例:
输入: nums = [1,2,3]
输出: [1,3,2]
输入: nums = [3,2,1]
输出: [1,2,3]
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        三步法实现
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,2,3]
            expected = [1,3,2]
            self.solution.nextPermutation(nums)
            self.assertEqual(nums, expected)
            
        def test_case2(self):
            nums = [3,2,1]
            expected = [1,2,3]
            self.solution.nextPermutation(nums)
            self.assertEqual(nums, expected)
            
    unittest.main()