"""
难度: medium
标签: 栈、数组、单调栈

题目描述:
给定一个整数数组 temperatures，表示每天的温度，返回一个数组 answer，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        单调栈解法
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        answer = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
            
        return answer


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            temps = [73,74,75,71,69,72,76,73]
            self.assertEqual(self.solution.dailyTemperatures(temps), [1,1,4,2,1,1,0,0])
            
        def test_case2(self):
            temps = [30,40,50,60]
            self.assertEqual(self.solution.dailyTemperatures(temps), [1,1,1,0])
            
    unittest.main()