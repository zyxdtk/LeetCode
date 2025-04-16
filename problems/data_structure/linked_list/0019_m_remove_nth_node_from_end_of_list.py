"""
难度: medium
标签: 链表、双指针

题目描述:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例:
输入: head = [1,2,3,4,5], n = 2
输出: [1,2,3,5]
输入: head = [1], n = 1
输出: []
输入: head = [1,2], n = 1
输出: [1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        使用快慢指针删除倒数第N个节点
        时间复杂度: O(L) L为链表长度
        空间复杂度: O(1)
        """
        dummy = ListNode(0, head)  # 哨兵节点处理头节点删除情况
        fast = slow = dummy
        
        # 快指针先移动n+1步
        for _ in range(n + 1):
            fast = fast.next
            
        # 同时移动快慢指针直到快指针到达末尾
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 删除slow.next节点
        slow.next = slow.next.next
        
        return dummy.next


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试删除倒数第2个节点
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            head.next.next.next.next = ListNode(5)
            
            result = self.solution.removeNthFromEnd(head, 2)
            # 验证结果: 1->2->3->5
            self.assertEqual(result.val, 1)
            self.assertEqual(result.next.val, 2)
            self.assertEqual(result.next.next.val, 3)
            self.assertEqual(result.next.next.next.val, 5)
            self.assertIsNone(result.next.next.next.next)
            
        def test_case2(self):
            # 测试删除唯一节点
            head = ListNode(1)
            result = self.solution.removeNthFromEnd(head, 1)
            self.assertIsNone(result)
            
        def test_case3(self):
            # 测试删除最后一个节点
            head = ListNode(1)
            head.next = ListNode(2)
            result = self.solution.removeNthFromEnd(head, 1)
            # 验证结果: 1
            self.assertEqual(result.val, 1)
            self.assertIsNone(result.next)
            
    unittest.main()