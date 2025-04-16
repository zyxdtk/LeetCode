"""
难度: easy
标签: 树、深度优先搜索、广度优先搜索、二叉树

题目描述:
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

示例:
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归法计算二叉树最大深度
        时间复杂度: O(n)
        空间复杂度: O(height) 递归栈空间
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: TreeNode) -> int:
        """
        广度优先搜索(BFS)计算二叉树最大深度
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not root:
            return 0
        
        depth = 0
        queue = [root]
        
        while queue:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return depth


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(3)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            
            self.assertEqual(self.solution.maxDepth(root), 3)
            self.assertEqual(self.solution.maxDepth_bfs(root), 3)
            
        def test_case2(self):
            # 测试空树
            self.assertEqual(self.solution.maxDepth(None), 0)
            self.assertEqual(self.solution.maxDepth_bfs(None), 0)
            
        def test_case3(self):
            # 测试只有根节点的树
            root = TreeNode(1)
            self.assertEqual(self.solution.maxDepth(root), 1)
            self.assertEqual(self.solution.maxDepth_bfs(root), 1)
            
    unittest.main()