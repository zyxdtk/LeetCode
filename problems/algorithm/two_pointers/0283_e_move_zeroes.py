"""
难度: easy
标签: 数组、双指针

题目描述:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
1. 必须在原数组上操作，不能拷贝额外的数组。
2. 尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [0, 1, 0, 3, 12]
            self.solution.moveZeroes(nums)
            self.assertEqual(nums, [1, 3, 12, 0, 0])

        def test_case2(self):
            nums = [0]
            self.solution.moveZeroes(nums)
            self.assertEqual(nums, [0])

        def test_case3(self):
            nums = [1, 2, 3]
            self.solution.moveZeroes(nums)
            self.assertEqual(nums, [1, 2, 3])

    unittest.main()
