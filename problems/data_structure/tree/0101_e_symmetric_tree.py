"""
难度: easy
标签: 树、深度优先搜索、广度优先搜索、二叉树

题目描述:
给定一个二叉树的根节点 root，检查它是否是镜像对称的。

示例:
输入: root = [1,2,2,3,4,4,3]
输出: true
输入: root = [1,2,2,null,3,null,3]
输出: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        递归法判断二叉树是否对称
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        if not root:
            return True
        return self._isMirror(root.left, root.right)
    
    def _isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                self._isMirror(left.left, right.right) and 
                self._isMirror(left.right, right.left))

    def isSymmetric_bfs(self, root: TreeNode) -> bool:
        """
        广度优先搜索(BFS)判断二叉树是否对称
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not root:
            return True
            
        queue = [root.left, root.right]
        
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
                
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
            
        return True


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建对称二叉树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(2)
            root.left.left = TreeNode(3)
            root.left.right = TreeNode(4)
            root.right.left = TreeNode(4)
            root.right.right = TreeNode(3)
            
            self.assertTrue(self.solution.isSymmetric(root))
            self.assertTrue(self.solution.isSymmetric_bfs(root))
            
        def test_case2(self):
            # 构建不对称二叉树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(2)
            root.left.right = TreeNode(3)
            root.right.right = TreeNode(3)
            
            self.assertFalse(self.solution.isSymmetric(root))
            self.assertFalse(self.solution.isSymmetric_bfs(root))
            
        def test_case3(self):
            # 测试空树
            self.assertTrue(self.solution.isSymmetric(None))
            self.assertTrue(self.solution.isSymmetric_bfs(None))
            
    unittest.main()