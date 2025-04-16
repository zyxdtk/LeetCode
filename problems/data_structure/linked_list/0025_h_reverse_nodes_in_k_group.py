"""
难度: hard
标签: 链表、递归

题目描述:
给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例:
输入: head = [1,2,3,4,5], k = 2
输出: [2,1,4,3,5]
输入: head = [1,2,3,4,5], k = 3
输出: [3,2,1,4,5]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        递归法实现K个一组翻转链表
        时间复杂度: O(n)
        空间复杂度: O(n/k) 递归栈空间
        """
        # 检查是否有足够的节点可以翻转
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
            
        if count == k:
            # 翻转当前k个节点
            reversed_head = self.reverse(head, k)
            # 递归处理后续节点
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        return head
    
    def reverse(self, head: ListNode, k: int) -> ListNode:
        """
        翻转前k个节点
        """
        prev = None
        curr = head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试k=2的情况
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            head.next.next.next.next = ListNode(5)
            
            result = self.solution.reverseKGroup(head, 2)
            # 验证结果: 2->1->4->3->5
            self.assertEqual(result.val, 2)
            self.assertEqual(result.next.val, 1)
            self.assertEqual(result.next.next.val, 4)
            self.assertEqual(result.next.next.next.val, 3)
            self.assertEqual(result.next.next.next.next.val, 5)
            self.assertIsNone(result.next.next.next.next.next)
            
        def test_case2(self):
            # 测试k=3的情况
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            head.next.next.next.next = ListNode(5)
            
            result = self.solution.reverseKGroup(head, 3)
            # 验证结果: 3->2->1->4->5
            self.assertEqual(result.val, 3)
            self.assertEqual(result.next.val, 2)
            self.assertEqual(result.next.next.val, 1)
            self.assertEqual(result.next.next.next.val, 4)
            self.assertEqual(result.next.next.next.next.val, 5)
            self.assertIsNone(result.next.next.next.next.next)
            
        def test_case3(self):
            # 测试k=1的情况(不翻转)
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            
            result = self.solution.reverseKGroup(head, 1)
            # 验证结果: 1->2->3
            self.assertEqual(result.val, 1)
            self.assertEqual(result.next.val, 2)
            self.assertEqual(result.next.next.val, 3)
            self.assertIsNone(result.next.next.next)
            
    unittest.main()