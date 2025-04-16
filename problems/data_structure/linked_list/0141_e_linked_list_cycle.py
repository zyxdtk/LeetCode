"""
难度: easy
标签: 链表、双指针

题目描述:
给你一个链表的头节点 head，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

示例:
输入: head = [3,2,0,-4], pos = 1 (表示尾节点连接到第1个节点)
输出: true
输入: head = [1], pos = -1 (表示没有环)
输出: false
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        使用快慢指针判断链表是否有环
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not head or not head.next:
            return False
            
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True


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
            self.assertTrue(self.solution.hasCycle(node1))
            
        def test_case2(self):
            # 测试无环链表: 1->2->3
            node1 = ListNode(1)
            node2 = ListNode(2)
            node3 = ListNode(3)
            node1.next = node2
            node2.next = node3
            self.assertFalse(self.solution.hasCycle(node1))
            
        def test_case3(self):
            # 测试单节点无环
            node1 = ListNode(1)
            self.assertFalse(self.solution.hasCycle(node1))
            
    unittest.main()