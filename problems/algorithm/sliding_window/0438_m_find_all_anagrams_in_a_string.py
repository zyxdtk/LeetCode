"""
难度: medium
标签: 哈希表、字符串、滑动窗口

题目描述:
给定两个字符串 s 和 p，找到 s 中所有 p 的字母异位词的子串，返回这些子串的起始索引。

示例:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
"""


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict

        res = []
        p_len = len(p)
        s_len = len(s)

        if s_len < p_len:
            return res

        p_count = defaultdict(int)
        window = defaultdict(int)

        for char in p:
            p_count[char] += 1

        for i in range(p_len):
            char = s[i]
            window[char] += 1

        if window == p_count:
            res.append(0)

        for i in range(p_len, s_len):
            left_char = s[i - p_len]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            right_char = s[i]
            window[right_char] += 1

            if window == p_count:
                res.append(i - p_len + 1)

        return res


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            s = "cbaebabacd"
            p = "abc"
            self.assertEqual(self.solution.findAnagrams(s, p), [0, 6])

        def test_case2(self):
            s = "abab"
            p = "ab"
            self.assertEqual(self.solution.findAnagrams(s, p), [0, 1, 2])

        def test_case3(self):
            s = "aa"
            p = "bb"
            self.assertEqual(self.solution.findAnagrams(s, p), [])

    unittest.main()
