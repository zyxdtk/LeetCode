"""
难度: medium
标签: 贪心算法、双指针、字符串

题目描述:
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例:
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
"""

from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
        贪心算法解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        last = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []
        
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
                
        return res


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            S = "ababcbacadefegdehijhklij"
            self.assertEqual(self.solution.partitionLabels(S), [9,7,8])
            
        def test_case2(self):
            S = "eccbbbbdec"
            self.assertEqual(self.solution.partitionLabels(S), [10])
            
    unittest.main()