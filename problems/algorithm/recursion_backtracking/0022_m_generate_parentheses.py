"""
难度: medium
标签: 字符串、动态规划、回溯算法

题目描述:
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例:
输入: n = 3
输出: ["((()))","(()())","(())()","()(())","()()()"]
输入: n = 1
输出: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        回溯算法实现
        时间复杂度: O(4^n/√n) 卡特兰数
        空间复杂度: O(n) 递归栈深度
        """
        def backtrack(left, right, path):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            if left < n:
                path.append('(')
                backtrack(left + 1, right, path)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(left, right + 1, path)
                path.pop()
                
        res = []
        backtrack(0, 0, [])
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            n = 3
            expected = ["((()))","(()())","(())()","()(())","()()()"]
            self.assertCountEqual(self.solution.generateParenthesis(n), expected)
            
        def test_case2(self):
            n = 1
            self.assertEqual(self.solution.generateParenthesis(n), ["()"])
            
    unittest.main()