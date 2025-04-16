"""
难度: easy
标签: 栈、字符串

题目描述:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

示例:
输入: s = "()"
输出: true
输入: s = "()[]{}"
输出: true
输入: s = "(]"
输出: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        使用栈验证括号有效性
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # 遇到右括号，弹出栈顶元素匹配
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # 遇到左括号，压入栈
                stack.append(char)
        
        # 栈为空说明全部匹配
        return not stack


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            self.assertTrue(self.solution.isValid("()"))
            
        def test_case2(self):
            self.assertTrue(self.solution.isValid("()[]{}"))
            
        def test_case3(self):
            self.assertFalse(self.solution.isValid("(]"))
            
        def test_case4(self):
            self.assertFalse(self.solution.isValid("([)]"))
            
        def test_case5(self):
            self.assertTrue(self.solution.isValid("{[]}"))
            
    unittest.main()