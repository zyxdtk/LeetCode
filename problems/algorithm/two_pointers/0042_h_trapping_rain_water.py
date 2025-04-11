"""
难度: hard
标签: 数组、双指针、动态规划、单调栈

题目描述:
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
解释: 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
            self.assertEqual(self.solution.trap(height), 6)

        def test_case2(self):
            height = [4, 2, 0, 3, 2, 5]
            self.assertEqual(self.solution.trap(height), 9)

        def test_case3(self):
            height = []
            self.assertEqual(self.solution.trap(height), 0)

    unittest.main()
