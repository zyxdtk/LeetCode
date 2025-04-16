"""
难度: medium
标签: 数组、排序

题目描述:
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
            expected = [[1, 6], [8, 10], [15, 18]]
            self.assertEqual(self.solution.merge(intervals), expected)

        def test_case2(self):
            intervals = [[1, 4], [4, 5]]
            expected = [[1, 5]]
            self.assertEqual(self.solution.merge(intervals), expected)

        def test_case3(self):
            intervals = []
            self.assertEqual(self.solution.merge(intervals), [])

    unittest.main()
