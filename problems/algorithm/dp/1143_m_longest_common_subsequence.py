"""
难度: medium
标签: 字符串、动态规划

题目描述:
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列，返回 0。

示例:
输入: text1 = "abcde", text2 = "ace" 
输出: 3  
解释: 最长公共子序列是 "ace"，它的长度为 3
输入: text1 = "abc", text2 = "def"
输出: 0
解释: 没有公共子序列，返回 0
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        动态规划解法
        时间复杂度: O(m*n)
        空间复杂度: O(m*n)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            text1 = "abcde"
            text2 = "ace"
            self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 3)
            
        def test_case2(self):
            text1 = "abc"
            text2 = "def"
            self.assertEqual(self.solution.longestCommonSubsequence(text1, text2), 0)
            
    unittest.main()