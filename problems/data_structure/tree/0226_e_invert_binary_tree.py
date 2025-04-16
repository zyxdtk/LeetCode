"""
难度: easy
标签: 树、深度优先搜索、广度优先搜索、二叉树

题目描述:
给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。

示例:
输入: root = [4,2,7,1,3,6,9]
输出: [4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        递归法翻转二叉树
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        if not root:
            return None
            
        # 交换左右子树
        root.left, root.right = root.right, root.left
        
        # 递归翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    def invertTree_bfs(self, root: TreeNode) -> TreeNode:
        """
        广度优先搜索(BFS)翻转二叉树
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not root:
            return None
            
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            # 交换左右子树
            node.left, node.right = node.right, node.left
            
            # 将子节点加入队列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(4)
            root.left = TreeNode(2)
            root.right = TreeNode(7)
            root.left.left = TreeNode(1)
            root.left.right = TreeNode(3)
            root.right.left = TreeNode(6)
            root.right.right = TreeNode(9)
            
            inverted = self.solution.invertTree(root)
            # 验证翻转结果
            self.assertEqual(inverted.val, 4)
            self.assertEqual(inverted.left.val, 7)
            self.assertEqual(inverted.right.val, 2)
            self.assertEqual(inverted.left.left.val, 9)
            self.assertEqual(inverted.left.right.val, 6)
            self.assertEqual(inverted.right.left.val, 3)
            self.assertEqual(inverted.right.right.val, 1)
            
        def test_case2(self):
            # 测试空树
            self.assertIsNone(self.solution.invertTree(None))
            
        def test_case3(self):
            # 测试只有根节点的树
            root = TreeNode(1)
            inverted = self.solution.invertTree(root)
            self.assertEqual(inverted.val, 1)
            self.assertIsNone(inverted.left)
            self.assertIsNone(inverted.right)
            
    unittest.main()