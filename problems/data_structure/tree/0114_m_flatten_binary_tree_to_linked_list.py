"""
难度: medium
标签: 栈、树、深度优先搜索、链表、二叉树

题目描述:
给你二叉树的根节点 root，请你将它展开为一个单链表：
1. 展开后的单链表应该同样使用 TreeNode，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null。
2. 展开后的单链表应该与二叉树先序遍历顺序相同。

示例:
输入: root = [1,2,5,3,4,null,6]
输出: [1,null,2,null,3,null,4,null,5,null,6]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        迭代法展开二叉树为链表
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                # 将右子树接到左子树的最右节点
                predecessor.right = curr.right
                # 将左子树移到右子树位置
                curr.right = curr.left
                curr.left = None
            # 移动到下一个节点
            curr = curr.right

    def flatten_recursive(self, root: TreeNode) -> None:
        """
        递归法展开二叉树为链表
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        def helper(node):
            if not node:
                return None
            # 展开左右子树
            left_last = helper(node.left)
            right_last = helper(node.right)
            # 如果有左子树，将其插入到当前节点和右子树之间
            if left_last:
                left_last.right = node.right
                node.right = node.left
                node.left = None
            # 返回最后一个节点
            return right_last or left_last or node
            
        helper(root)


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(5)
            root.left.left = TreeNode(3)
            root.left.right = TreeNode(4)
            root.right.right = TreeNode(6)
            
            self.solution.flatten(root)
            # 验证展开结果
            self.assertEqual(root.val, 1)
            self.assertIsNone(root.left)
            self.assertEqual(root.right.val, 2)
            self.assertEqual(root.right.right.val, 3)
            self.assertEqual(root.right.right.right.val, 4)
            self.assertEqual(root.right.right.right.right.val, 5)
            self.assertEqual(root.right.right.right.right.right.val, 6)
            self.assertIsNone(root.right.right.right.right.right.right)
            
        def test_case2(self):
            # 测试空树
            self.assertIsNone(self.solution.flatten(None))
            
        def test_case3(self):
            # 测试只有右子树的树
            root = TreeNode(1)
            root.right = TreeNode(2)
            root.right.right = TreeNode(3)
            
            self.solution.flatten(root)
            self.assertEqual(root.val, 1)
            self.assertEqual(root.right.val, 2)
            self.assertEqual(root.right.right.val, 3)
            
    unittest.main()