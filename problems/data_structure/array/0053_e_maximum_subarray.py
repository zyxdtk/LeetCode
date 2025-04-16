"""
难度: easy
标签: 数组、分治、动态规划

题目描述:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
            self.assertEqual(self.solution.maxSubArray(nums), 6)

        def test_case2(self):
            nums = [1]
            self.assertEqual(self.solution.maxSubArray(nums), 1)

        def test_case3(self):
            nums = [-1, -2]
            self.assertEqual(self.solution.maxSubArray(nums), -1)

    unittest.main()
