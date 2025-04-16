"""
难度: medium
标签: 树、深度优先搜索、二叉树

题目描述:
给定一个二叉树的根节点 root，和一个整数 targetSum，求该二叉树里节点值之和等于 targetSum 的路径的数目。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例:
输入: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出: 3
解释: 和为8的路径有: 5→3, 5→2→1, -3→11
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        前缀和+DFS解法
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        from collections import defaultdict
        self.count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
            self.count += prefix_sum[current_sum - targetSum]
            prefix_sum[current_sum] += 1
            
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            prefix_sum[current_sum] -= 1
            
        dfs(root, 0)
        return self.count


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(10)
            root.left = TreeNode(5)
            root.right = TreeNode(-3)
            root.left.left = TreeNode(3)
            root.left.right = TreeNode(2)
            root.right.right = TreeNode(11)
            root.left.left.left = TreeNode(3)
            root.left.left.right = TreeNode(-2)
            root.left.right.right = TreeNode(1)
            
            self.assertEqual(self.solution.pathSum(root, 8), 3)
            
        def test_case2(self):
            # 测试空树
            self.assertEqual(self.solution.pathSum(None, 1), 0)
            
        def test_case3(self):
            # 测试单节点树
            root = TreeNode(1)
            self.assertEqual(self.solution.pathSum(root, 1), 1)
            
    unittest.main()