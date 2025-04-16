"""
难度: medium
标签: 栈、递归、字符串

题目描述:
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。k 保证为正整数。

示例:
输入: s = "3[a]2[bc]"
输出: "aaabcbc"
输入: s = "3[a2[c]]"
输出: "accaccacc"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
        使用栈结构解码字符串
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += char
                
        return curr_str


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            self.assertEqual(self.solution.decodeString("3[a]2[bc]"), "aaabcbc")
            
        def test_case2(self):
            self.assertEqual(self.solution.decodeString("3[a2[c]]"), "accaccacc")
            
        def test_case3(self):
            self.assertEqual(self.solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
            
    unittest.main()