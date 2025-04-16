"""
难度: hard
标签: 数组、哈希表

题目描述:
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

示例:
输入: nums = [1,2,0]
输出: 3
输入: nums = [3,4,-1,1]
输出: 2
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # 将数组视为哈希表
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 检查第一个不符合nums[i] == i+1的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [1, 2, 0]
            self.assertEqual(self.solution.firstMissingPositive(nums), 3)

        def test_case2(self):
            nums = [3, 4, -1, 1]
            self.assertEqual(self.solution.firstMissingPositive(nums), 2)

        def test_case3(self):
            nums = [7, 8, 9, 11, 12]
            self.assertEqual(self.solution.firstMissingPositive(nums), 1)

    unittest.main()
