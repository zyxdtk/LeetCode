"""
难度: medium
标签: 链表、双指针、分治、排序

题目描述:
给你链表的头结点 head，请将其按升序排列并返回排序后的链表。

示例:
输入: head = [4,2,1,3]
输出: [1,2,3,4]
输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        使用归并排序算法对链表进行排序
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        if not head or not head.next:
            return head
            
        # 使用快慢指针找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 分割链表
        mid = slow.next
        slow.next = None
        
        # 递归排序左右两部分
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 合并两个有序链表
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并两个有序链表
        """
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 if l1 else l2
        return dummy.next


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试正常排序
            head = ListNode(4)
            head.next = ListNode(2)
            head.next.next = ListNode(1)
            head.next.next.next = ListNode(3)
            
            result = self.solution.sortList(head)
            # 验证结果: 1->2->3->4
            self.assertEqual(result.val, 1)
            self.assertEqual(result.next.val, 2)
            self.assertEqual(result.next.next.val, 3)
            self.assertEqual(result.next.next.next.val, 4)
            self.assertIsNone(result.next.next.next.next)
            
        def test_case2(self):
            # 测试负数排序
            head = ListNode(-1)
            head.next = ListNode(5)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            head.next.next.next.next = ListNode(0)
            
            result = self.solution.sortList(head)
            # 验证结果: -1->0->3->4->5
            self.assertEqual(result.val, -1)
            self.assertEqual(result.next.val, 0)
            self.assertEqual(result.next.next.val, 3)
            self.assertEqual(result.next.next.next.val, 4)
            self.assertEqual(result.next.next.next.next.val, 5)
            self.assertIsNone(result.next.next.next.next.next)
            
    unittest.main()