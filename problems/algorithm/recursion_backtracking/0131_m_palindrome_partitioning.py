"""
难度: medium
标签: 字符串、动态规划、回溯算法

题目描述:
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。

示例:
输入: s = "aab"
输出: [["a","a","b"],["aa","b"]]
输入: s = "a"
输出: [["a"]]
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        回溯算法实现
        时间复杂度: O(n*2^n)
        空间复杂度: O(n^2)
        """
        def is_palindrome(subs):
            return subs == subs[::-1]
            
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                substr = s[start:end]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()
                    
        res = []
        backtrack(0, [])
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            s = "aab"
            expected = [["a","a","b"],["aa","b"]]
            self.assertCountEqual(self.solution.partition(s), expected)
            
        def test_case2(self):
            s = "a"
            self.assertEqual(self.solution.partition(s), [["a"]])
            
    unittest.main()