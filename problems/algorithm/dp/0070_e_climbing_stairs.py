"""
难度: easy
标签: 记忆化、数学、动态规划

题目描述:
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例:
输入: n = 2
输出: 2
解释: 有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
输入: n = 3
输出: 3
解释: 有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        动态规划解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if n <= 2:
            return n
            
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            self.assertEqual(self.solution.climbStairs(2), 2)
            
        def test_case2(self):
            self.assertEqual(self.solution.climbStairs(3), 3)
            
        def test_case3(self):
            self.assertEqual(self.solution.climbStairs(4), 5)
            
    unittest.main()