"""
难度: medium
标签: 字典树、记忆化、哈希表、字符串、动态规划

题目描述:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

示例:
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        动态规划解法
        时间复杂度: O(n^2)
        空间复杂度: O(n)
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            s = "leetcode"
            wordDict = ["leet", "code"]
            self.assertTrue(self.solution.wordBreak(s, wordDict))
            
        def test_case2(self):
            s = "applepenapple"
            wordDict = ["apple", "pen"]
            self.assertTrue(self.solution.wordBreak(s, wordDict))
            
    unittest.main()