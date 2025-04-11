"""
难度: easy
标签: 数组、哈希表

题目描述:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [2, 7, 11, 15]
            target = 9
            self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

        def test_case2(self):
            nums = [3, 2, 4]
            target = 6
            self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

        def test_case3(self):
            nums = [3, 3]
            target = 6
            self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    unittest.main()
