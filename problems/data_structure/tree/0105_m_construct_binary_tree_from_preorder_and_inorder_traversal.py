"""
难度: medium
标签: 树、数组、哈希表、分治、二叉树

题目描述:
给定两个整数数组 preorder 和 inorder，其中 preorder 是二叉树的先序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归法构建二叉树
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        # 构建中序遍历的值到索引的映射
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
                
            # 前序遍历的第一个元素是根节点
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            in_root_idx = inorder_map[root_val]
            left_size = in_root_idx - in_start
            
            # 递归构建左右子树
            root.left = helper(pre_start + 1, pre_start + left_size, 
                             in_start, in_root_idx - 1)
            root.right = helper(pre_start + left_size + 1, pre_end,
                              in_root_idx + 1, in_end)
            
            return root
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            preorder = [3,9,20,15,7]
            inorder = [9,3,15,20,7]
            root = self.solution.buildTree(preorder, inorder)
            
            # 验证树的结构
            self.assertEqual(root.val, 3)
            self.assertEqual(root.left.val, 9)
            self.assertEqual(root.right.val, 20)
            self.assertEqual(root.right.left.val, 15)
            self.assertEqual(root.right.right.val, 7)
            
        def test_case2(self):
            preorder = [-1]
            inorder = [-1]
            root = self.solution.buildTree(preorder, inorder)
            self.assertEqual(root.val, -1)
            self.assertIsNone(root.left)
            self.assertIsNone(root.right)
            
    unittest.main()