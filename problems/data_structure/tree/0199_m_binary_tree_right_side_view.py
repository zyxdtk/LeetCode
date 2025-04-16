"""
难度: medium
标签: 树、深度优先搜索、广度优先搜索、二叉树

题目描述:
给定一棵二叉树的根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
解释:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        广度优先搜索(BFS)实现右视图
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                # 只记录每层最后一个节点
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result

    def rightSideView_dfs(self, root: TreeNode) -> List[int]:
        """
        深度优先搜索(DFS)实现右视图
        时间复杂度: O(n)
        空间复杂度: O(h) h为树的高度
        """
        result = []
        def dfs(node, depth):
            if not node:
                return
            # 每层第一次访问的节点就是最右侧节点
            if depth == len(result):
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试二叉树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            root.left.right = TreeNode(5)
            root.right.right = TreeNode(4)
            
            self.assertEqual(self.solution.rightSideView(root), [1,3,4])
            
        def test_case2(self):
            # 测试空树
            self.assertEqual(self.solution.rightSideView(None), [])
            
        def test_case3(self):
            # 测试只有左子树的树
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.left.left = TreeNode(3)
            
            self.assertEqual(self.solution.rightSideView(root), [1,2,3])
            
    unittest.main()