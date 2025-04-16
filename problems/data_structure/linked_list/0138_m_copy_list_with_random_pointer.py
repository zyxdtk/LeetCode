"""
难度: medium
标签: 链表、哈希表

题目描述:
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random，该指针可以指向链表中的任何节点或空节点。
构造这个链表的深拷贝。深拷贝应该正好由 n 个全新节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点。

示例:
输入: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        使用哈希表存储原节点和复制节点的映射关系
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not head:
            return None
            
        # 创建原节点到复制节点的映射
        node_map = {}
        
        # 第一次遍历：创建所有节点并建立映射
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
            
        # 第二次遍历：设置next和random指针
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
            
        return node_map[head]


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试链表
            node1 = Node(7)
            node2 = Node(13)
            node3 = Node(11)
            node4 = Node(10)
            node5 = Node(1)
            
            node1.next = node2
            node2.next = node3
            node3.next = node4
            node4.next = node5
            
            node1.random = None
            node2.random = node1
            node3.random = node5
            node4.random = node3
            node5.random = node1
            
            # 复制链表
            copied = self.solution.copyRandomList(node1)
            
            # 验证复制结果
            self.assertEqual(copied.val, 7)
            self.assertIsNone(copied.random)
            self.assertEqual(copied.next.val, 13)
            self.assertEqual(copied.next.random.val, 7)
            self.assertEqual(copied.next.next.val, 11)
            self.assertEqual(copied.next.next.random.val, 1)
            self.assertEqual(copied.next.next.next.val, 10)
            self.assertEqual(copied.next.next.next.random.val, 11)
            self.assertEqual(copied.next.next.next.next.val, 1)
            self.assertEqual(copied.next.next.next.next.random.val, 7)
            
    unittest.main()