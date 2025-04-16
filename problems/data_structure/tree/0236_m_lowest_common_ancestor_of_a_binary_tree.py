"""
难度: medium
标签: 树、深度优先搜索、二叉树

题目描述:
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

示例:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点5和节点1的最近公共祖先是节点3。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        递归法查找最近公共祖先
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        if not root or root == p or root == q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(3)
            root.left = TreeNode(5)
            root.right = TreeNode(1)
            root.left.left = TreeNode(6)
            root.left.right = TreeNode(2)
            root.right.left = TreeNode(0)
            root.right.right = TreeNode(8)
            root.left.right.left = TreeNode(7)
            root.left.right.right = TreeNode(4)
            
            p = root.left  # 5
            q = root.right  # 1
            self.assertEqual(self.solution.lowestCommonAncestor(root, p, q).val, 3)
            
        def test_case2(self):
            # 测试一个节点是另一个节点的祖先
            root = TreeNode(1)
            root.left = TreeNode(2)
            p = root
            q = root.left
            self.assertEqual(self.solution.lowestCommonAncestor(root, p, q).val, 1)
            
    unittest.main()