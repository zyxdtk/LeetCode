"""
难度: medium
标签: 树、深度优先搜索、二叉搜索树、二叉树

题目描述:
给定一个二叉搜索树的根节点 root 和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从1开始计数）。

示例:
输入: root = [3,1,4,null,2], k = 1
输出: 1
输入: root = [5,3,6,2,4,null,null,1], k = 3
输出: 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        迭代法中序遍历查找第K小元素
        时间复杂度: O(H + k) H是树的高度
        空间复杂度: O(H)
        """
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

    def kthSmallest_recursive(self, root: TreeNode, k: int) -> int:
        """
        递归法中序遍历查找第K小元素
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
            
        return inorder(root)[k-1]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试BST
            root = TreeNode(3)
            root.left = TreeNode(1)
            root.right = TreeNode(4)
            root.left.right = TreeNode(2)
            
            self.assertEqual(self.solution.kthSmallest(root, 1), 1)
            
        def test_case2(self):
            # 构建测试BST
            root = TreeNode(5)
            root.left = TreeNode(3)
            root.right = TreeNode(6)
            root.left.left = TreeNode(2)
            root.left.right = TreeNode(4)
            root.left.left.left = TreeNode(1)
            
            self.assertEqual(self.solution.kthSmallest(root, 3), 3)
            
        def test_case3(self):
            # 测试单节点树
            root = TreeNode(1)
            self.assertEqual(self.solution.kthSmallest(root, 1), 1)
            
    unittest.main()