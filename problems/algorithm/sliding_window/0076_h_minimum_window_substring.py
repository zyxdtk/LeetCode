"""
难度: hard
标签: 哈希表、字符串、滑动窗口

题目描述:
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""。

示例:
输入: s = "ADOBECODEBANC", t = "ABC"
输出: "BANC"
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict

        need = defaultdict(int)
        for char in t:
            need[char] += 1
        need_cnt = len(t)

        res = ""
        left = 0
        min_len = float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                need_cnt -= 1
            need[char] -= 1

            while need_cnt == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left : right + 1]

                if need[s[left]] == 0:
                    need_cnt += 1
                need[s[left]] += 1
                left += 1

        return res


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            s = "ADOBECODEBANC"
            t = "ABC"
            self.assertEqual(self.solution.minWindow(s, t), "BANC")

        def test_case2(self):
            s = "a"
            t = "a"
            self.assertEqual(self.solution.minWindow(s, t), "a")

        def test_case3(self):
            s = "a"
            t = "aa"
            self.assertEqual(self.solution.minWindow(s, t), "")

    unittest.main()
