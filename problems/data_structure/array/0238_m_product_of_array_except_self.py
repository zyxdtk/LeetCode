"""
难度: medium
标签: 数组、前缀和

题目描述:
给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        # 计算左侧乘积
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 计算右侧乘积并乘以左侧乘积
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [1, 2, 3, 4]
            self.assertEqual(self.solution.productExceptSelf(nums), [24, 12, 8, 6])

        def test_case2(self):
            nums = [-1, 1, 0, -3, 3]
            self.assertEqual(self.solution.productExceptSelf(nums), [0, 0, 9, 0, 0])

        def test_case3(self):
            nums = [1, 1]
            self.assertEqual(self.solution.productExceptSelf(nums), [1, 1])

    unittest.main()
