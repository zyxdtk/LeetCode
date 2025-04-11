"""
难度: hard
标签: 数组、哈希表、并查集

题目描述:
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]，长度为4。
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:  # 确保是序列的起点
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [100, 4, 200, 1, 3, 2]
            self.assertEqual(self.solution.longestConsecutive(nums), 4)

        def test_case2(self):
            nums = [0, -1]
            self.assertEqual(self.solution.longestConsecutive(nums), 2)

        def test_case3(self):
            nums = []
            self.assertEqual(self.solution.longestConsecutive(nums), 0)

    unittest.main()
