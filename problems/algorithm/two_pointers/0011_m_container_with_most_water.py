"""
难度: medium
标签: 数组、双指针

题目描述:
给定一个长度为n的整数数组height。有n条垂线，第i条线的两个端点是(i, 0)和(i, height[i])。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
解释: 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水的最大值为49。
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
            self.assertEqual(self.solution.maxArea(height), 49)

        def test_case2(self):
            height = [1, 1]
            self.assertEqual(self.solution.maxArea(height), 1)

        def test_case3(self):
            height = [4, 3, 2, 1, 4]
            self.assertEqual(self.solution.maxArea(height), 16)

    unittest.main()
