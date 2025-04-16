"""
难度: medium
标签: 字符串、动态规划

题目描述:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例:
输入: "babad"
输出: "bab" 或 "aba"
输入: "cbbd"
输出: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        动态规划解法
        时间复杂度: O(n^2)
        空间复杂度: O(n^2)
        """
        n = len(s)
        if n < 2:
            return s
            
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        
        # 所有长度为1的子串都是回文
        for i in range(n):
            dp[i][i] = True
            
        # 检查长度为2的子串
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
                
        # 检查长度大于2的子串
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length
                        
        return s[start:start+max_len]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            s = "babad"
            result = self.solution.longestPalindrome(s)
            self.assertTrue(result == "bab" or result == "aba")
            
        def test_case2(self):
            s = "cbbd"
            self.assertEqual(self.solution.longestPalindrome(s), "bb")
            
    unittest.main()