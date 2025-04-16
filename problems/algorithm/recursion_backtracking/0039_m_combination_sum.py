"""
难度: medium
标签: 数组、回溯算法

题目描述:
给定一个无重复元素的整数数组 candidates 和一个目标整数 target，找出 candidates 中所有可以使数字和等于 target 的组合。candidates 中的数字可以无限制重复被选取。

示例:
输入: candidates = [2,3,6,7], target = 7
输出: [[2,2,3],[7]]
解释: 2+2+3=7, 7=7
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯算法实现
        时间复杂度: O(n^target)
        空间复杂度: O(target)
        """
        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                path.append(candidates[i])
                backtrack(i, path, remain - candidates[i])
                path.pop()
                
        res = []
        candidates.sort()
        backtrack(0, [], target)
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            candidates = [2,3,6,7]
            target = 7
            expected = [[2,2,3],[7]]
            self.assertCountEqual(self.solution.combinationSum(candidates, target), expected)
            
        def test_case2(self):
            candidates = [2,3,5]
            target = 8
            expected = [[2,2,2,2],[2,3,3],[3,5]]
            self.assertCountEqual(self.solution.combinationSum(candidates, target), expected)
            
    unittest.main()