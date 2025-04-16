"""
难度: easy
标签: 树、二叉搜索树、数组、分治、二叉树

题目描述:
给你一个整数数组 nums，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。

示例:
输入: nums = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是 [0,-3,9,-10,null,5]，它表示的高度平衡的二叉搜索树。
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        递归法构建高度平衡二叉搜索树
        时间复杂度: O(n)
        空间复杂度: O(log n) 递归栈空间
        """
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
            
        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [-10,-3,0,5,9]
            root = self.solution.sortedArrayToBST(nums)
            # 验证树的高度平衡性
            self.assertTrue(self.isBalanced(root))
            # 验证是二叉搜索树
            self.assertTrue(self.isBST(root))
            
        def test_case2(self):
            nums = [1,3]
            root = self.solution.sortedArrayToBST(nums)
            self.assertTrue(self.isBalanced(root))
            self.assertTrue(self.isBST(root))
            
        def isBalanced(self, root: TreeNode) -> bool:
            def check(node):
                if not node:
                    return 0
                left = check(node.left)
                right = check(node.right)
                if left == -1 or right == -1 or abs(left - right) > 1:
                    return -1
                return max(left, right) + 1
            return check(root) != -1
            
        def isBST(self, root: TreeNode) -> bool:
            def validate(node, low=float('-inf'), high=float('inf')):
                if not node:
                    return True
                if node.val <= low or node.val >= high:
                    return False
                return (validate(node.left, low, node.val) and 
                        validate(node.right, node.val, high))
            return validate(root)
            
    unittest.main()