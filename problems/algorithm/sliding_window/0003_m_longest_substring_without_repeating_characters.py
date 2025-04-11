"""
难度: medium
标签: 哈希表、字符串、滑动窗口

题目描述:
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            s = "abcabcbb"
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

        def test_case2(self):
            s = "bbbbb"
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), 1)

        def test_case3(self):
            s = "pwwkew"
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), 3)

    unittest.main()
