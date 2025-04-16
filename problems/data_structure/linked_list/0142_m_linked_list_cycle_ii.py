"""
难度: medium
标签: 链表、双指针

题目描述:
给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回 null。

示例:
输入: head = [3,2,0,-4], pos = 1 (表示尾节点连接到第1个节点)
输出: 返回索引为1的节点
输入: head = [1], pos = -1 (表示没有环)
输出: 返回null
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        使用快慢指针找到环的入口节点
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not head or not head.next:
            return None
            
        slow = fast = head
        has_cycle = False
        
        # 第一阶段：判断是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
                
        if not has_cycle:
            return None
            
        # 第二阶段：找到环的入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试有环链表: 3->2->0->-4->2...
            node1 = ListNode(3)
            node2 = ListNode(2)
            node3 = ListNode(0)
            node4 = ListNode(-4)
            node1.next = node2
            node2.next = node3
            node3.next = node4
            node4.next = node2
            self.assertEqual(self.solution.detectCycle(node1), node2)
            
        def test_case2(self):
            # 测试无环链表: 1->2->3
            node1 = ListNode(1)
            node2 = ListNode(2)
            node3 = ListNode(3)
            node1.next = node2
            node2.next = node3
            self.assertIsNone(self.solution.detectCycle(node1))
            
        def test_case3(self):
            # 测试单节点无环
            node1 = ListNode(1)
            self.assertIsNone(self.solution.detectCycle(node1))
            
    unittest.main()