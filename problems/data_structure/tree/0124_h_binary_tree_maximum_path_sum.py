"""
难度: hard
标签: 树、深度优先搜索、动态规划、二叉树

题目描述:
给定一个非空二叉树，返回其最大路径和。
路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例:
输入: [1,2,3]
       1
      / \
     2   3
输出: 6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        递归法计算最大路径和
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
                
            # 计算左右子树的最大贡献值
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 当前节点作为路径连接点的最大和
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_newpath)
            
            # 返回当前节点的最大贡献值
            return node.val + max(left_gain, right_gain)
            
        max_gain(root)
        return self.max_sum


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            self.assertEqual(self.solution.maxPathSum(root), 6)
            
        def test_case2(self):
            # 测试负值节点
            root = TreeNode(-10)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            self.assertEqual(self.solution.maxPathSum(root), 42)
            
        def test_case3(self):
            # 测试单节点树
            root = TreeNode(-3)
            self.assertEqual(self.solution.maxPathSum(root), -3)
            
    unittest.main()