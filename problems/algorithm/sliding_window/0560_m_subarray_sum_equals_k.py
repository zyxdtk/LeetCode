"""
难度: medium
标签: 数组、哈希表、前缀和

题目描述:
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续子数组的个数。

示例:
输入: nums = [1,1,1], k = 2
输出: 2
解释: [1,1] 与 [1,1] 为两种不同的情况。
"""


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        prefix_sum = 0
        count = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            sum_count[prefix_sum] += 1

        return count


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [1, 1, 1]
            k = 2
            self.assertEqual(self.solution.subarraySum(nums, k), 2)

        def test_case2(self):
            nums = [1, 2, 3]
            k = 3
            self.assertEqual(self.solution.subarraySum(nums, k), 2)

        def test_case3(self):
            nums = [1, -1, 0]
            k = 0
            self.assertEqual(self.solution.subarraySum(nums, k), 3)

    unittest.main()
