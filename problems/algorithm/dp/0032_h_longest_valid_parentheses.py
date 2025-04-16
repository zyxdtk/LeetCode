"""
难度: hard
标签: 栈、字符串、动态规划

题目描述:
给定一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        动态规划解法
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not s:
            return 0
            
        dp = [0] * len(s)
        max_len = 0
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if (i - dp[i-1]) >= 2 else 0)
                max_len = max(max_len, dp[i])
                
        return max_len


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            s = "(()"
            self.assertEqual(self.solution.longestValidParentheses(s), 2)
            
        def test_case2(self):
            s = ")()())"
            self.assertEqual(self.solution.longestValidParentheses(s), 4)
            
    unittest.main()