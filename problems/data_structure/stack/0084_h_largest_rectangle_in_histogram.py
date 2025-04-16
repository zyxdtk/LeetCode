"""
难度: hard
标签: 栈、数组、单调栈

题目描述:
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为1。求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: heights = [2,1,5,6,2,3]
输出: 10
解释: 最大的矩形面积为10（高度5，宽度2）
输入: heights = [2,4]
输出: 4
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调栈解法
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        max_area = 0
        heights = [0] + heights + [0]  # 添加哨兵节点
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
            
        return max_area


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            heights = [2,1,5,6,2,3]
            self.assertEqual(self.solution.largestRectangleArea(heights), 10)
            
        def test_case2(self):
            heights = [2,4]
            self.assertEqual(self.solution.largestRectangleArea(heights), 4)
            
    unittest.main()