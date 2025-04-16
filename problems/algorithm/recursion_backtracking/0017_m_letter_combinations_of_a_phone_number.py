"""
难度: medium
标签: 哈希表、字符串、回溯算法

题目描述:
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按任意顺序返回。
数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

示例:
输入: digits = "23"
输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
输入: digits = ""
输出: []
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        回溯算法实现
        时间复杂度: O(3^m * 4^n) m是3字母数字个数，n是4字母数字个数
        空间复杂度: O(m+n) 递归栈深度
        """
        if not digits:
            return []
            
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return
            for char in digit_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
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
            digits = "23"
            expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
            self.assertCountEqual(self.solution.letterCombinations(digits), expected)
            
        def test_case2(self):
            digits = ""
            self.assertEqual(self.solution.letterCombinations(digits), [])
            
    unittest.main()