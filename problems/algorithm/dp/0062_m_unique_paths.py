"""
难度: medium
标签: 数组、动态规划

题目描述:
一个机器人位于一个 m x n 网格的左上角，机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。问总共有多少条不同的路径？

示例:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角：
1. 右 -> 下 -> 下
2. 下 -> 右 -> 下
3. 下 -> 下 -> 右
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        动态规划解法
        时间复杂度: O(m*n)
        空间复杂度: O(n)
        """
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
                
        return dp[-1] if n > 0 else 0


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            self.assertEqual(self.solution.uniquePaths(3, 2), 3)
            
        def test_case2(self):
            self.assertEqual(self.solution.uniquePaths(7, 3), 28)
            
    unittest.main()