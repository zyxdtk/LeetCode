"""
难度: medium
标签: 树、深度优先搜索、二叉搜索树、二叉树

题目描述:
给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。

示例:
输入: root = [2,1,3]
输出: true
输入: root = [5,1,4,null,null,3,6]
输出: false
解释: 根节点的值是5，但是右子节点的值是4。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        中序遍历验证二叉搜索树
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        prev = None
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and curr.val <= prev.val:
                return False
            prev = curr
            curr = curr.right
            
        return True

    def isValidBST_recursive(self, root: TreeNode) -> bool:
        """
        递归验证二叉搜索树
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        return validate(root)


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建有效的BST
            root = TreeNode(2)
            root.left = TreeNode(1)
            root.right = TreeNode(3)
            self.assertTrue(self.solution.isValidBST(root))
            
        def test_case2(self):
            # 构建无效的BST
            root = TreeNode(5)
            root.left = TreeNode(1)
            root.right = TreeNode(4)
            root.right.left = TreeNode(3)
            root.right.right = TreeNode(6)
            self.assertFalse(self.solution.isValidBST(root))
            
        def test_case3(self):
            # 测试空树
            self.assertTrue(self.solution.isValidBST(None))
            
    unittest.main()