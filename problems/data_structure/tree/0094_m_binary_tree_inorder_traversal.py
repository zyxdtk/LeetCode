"""
难度: medium
标签: 栈、树、深度优先搜索、二叉树

题目描述:
给定一个二叉树的根节点 root，返回它的中序遍历。

示例:
输入: root = [1,null,2,3]
输出: [1,3,2]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代法中序遍历二叉树
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # 先遍历到最左节点
            while curr:
                stack.append(curr)
                curr = curr.left
            # 弹出栈顶元素并访问
            curr = stack.pop()
            res.append(curr.val)
            # 转向右子树
            curr = curr.right
            
        return res

    def inorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        """
        递归法中序遍历二叉树
        时间复杂度: O(n)
        空间复杂度: O(n) 递归栈空间
        """
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树: 1 -> null -> 2 -> 3
            root = TreeNode(1)
            root.right = TreeNode(2)
            root.right.left = TreeNode(3)
            
            result = self.solution.inorderTraversal(root)
            self.assertEqual(result, [1,3,2])
            
        def test_case2(self):
            # 测试空树
            self.assertEqual(self.solution.inorderTraversal(None), [])
            
        def test_case3(self):
            # 测试只有根节点的树
            root = TreeNode(1)
            self.assertEqual(self.solution.inorderTraversal(root), [1])
            
    unittest.main()