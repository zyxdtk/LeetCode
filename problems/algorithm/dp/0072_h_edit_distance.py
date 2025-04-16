"""
难度: hard
标签: 字符串、动态规划

题目描述:
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数。你可以对一个单词进行如下三种操作：
1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

示例:
输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
输入: word1 = "intention", word2 = "execution"
输出: 5
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划解法
        时间复杂度: O(m*n)
        空间复杂度: O(m*n)
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化边界条件
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # 删除
                        dp[i][j-1],    # 插入
                        dp[i-1][j-1]   # 替换
                    )
                    
        return dp[m][n]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            word1 = "horse"
            word2 = "ros"
            self.assertEqual(self.solution.minDistance(word1, word2), 3)
            
        def test_case2(self):
            word1 = "intention"
            word2 = "execution"
            self.assertEqual(self.solution.minDistance(word1, word2), 5)
            
    unittest.main()