"""
难度: medium
标签: 数组、双指针

题目描述:
给定一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [1, 2, 3, 4, 5, 6, 7]
            k = 3
            self.solution.rotate(nums, k)
            self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

        def test_case2(self):
            nums = [-1, -100, 3, 99]
            k = 2
            self.solution.rotate(nums, k)
            self.assertEqual(nums, [3, 99, -1, -100])

        def test_case3(self):
            nums = [1, 2]
            k = 3
            self.solution.rotate(nums, k)
            self.assertEqual(nums, [2, 1])

    unittest.main()
