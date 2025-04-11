"""
难度: medium
标签: 数组、双指针、排序

题目描述:
给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c，使得a + b + c = 0？请你找出所有和为0且不重复的三元组。

示例:
输入: nums = [-1,0,1,2,-1,-4]
输出: [[-1,-1,2],[-1,0,1]]
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [-1, 0, 1, 2, -1, -4]
            expected = [[-1, -1, 2], [-1, 0, 1]]
            self.assertEqual(self.solution.threeSum(nums), expected)

        def test_case2(self):
            nums = []
            self.assertEqual(self.solution.threeSum(nums), [])

        def test_case3(self):
            nums = [0]
            self.assertEqual(self.solution.threeSum(nums), [])

    unittest.main()
