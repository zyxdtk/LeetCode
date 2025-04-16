"""
难度: easy
标签: 树、深度优先搜索、二叉树

题目描述:
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例:
给定二叉树:
          1
         / \
        2   3
       / \     
      4   5    
返回 3，它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        递归计算二叉树直径
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        self.max_diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 更新最大直径
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
            
        depth(root)
        return self.max_diameter


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
            root.left.left = TreeNode(4)
            root.left.right = TreeNode(5)
            
            self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)
            
        def test_case2(self):
            # 测试单节点树
            root = TreeNode(1)
            self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)
            
        def test_case3(self):
            # 测试空树
            self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)
            
    unittest.main()