"""
难度: medium
标签: 树、广度优先搜索、二叉树

题目描述:
给你二叉树的根节点 root，返回其节点值的层序遍历。(即逐层地，从左到右访问所有节点)。

示例:
输入: root = [3,9,20,null,null,15,7]
输出: [[3],[9,20],[15,7]]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        广度优先搜索(BFS)实现层序遍历
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            
        return result


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(3)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            
            expected = [[3], [9,20], [15,7]]
            self.assertEqual(self.solution.levelOrder(root), expected)
            
        def test_case2(self):
            # 测试空树
            self.assertEqual(self.solution.levelOrder(None), [])
            
        def test_case3(self):
            # 测试只有根节点的树
            root = TreeNode(1)
            self.assertEqual(self.solution.levelOrder(root), [[1]])
            
    unittest.main()