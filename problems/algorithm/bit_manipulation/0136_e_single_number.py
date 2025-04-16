"""
难度: easy
标签: 位运算、数组

题目描述:
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

示例:
输入: [2,2,1]
输出: 1
输入: [4,1,2,1,2]
输出: 4
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        位运算解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    import unittest
    from typing import List

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [2, 2, 1]
            self.assertEqual(self.solution.singleNumber(nums), 1)

        def test_case2(self):
            nums = [4, 1, 2, 1, 2]
            self.assertEqual(self.solution.singleNumber(nums), 4)

    unittest.main()
