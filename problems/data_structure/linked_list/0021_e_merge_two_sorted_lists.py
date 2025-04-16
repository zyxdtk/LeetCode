"""
难度: easy
标签: 链表、递归

题目描述:
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例:
输入: l1 = [1,2,4], l2 = [1,3,4]
输出: [1,1,2,3,4,4]
输入: l1 = [], l2 = []
输出: []
输入: l1 = [], l2 = [0]
输出: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代法合并两个有序链表
        时间复杂度: O(n+m)
        空间复杂度: O(1)
        """
        dummy = ListNode(-1)  # 哨兵节点
        prev = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        # 连接剩余节点
        prev.next = l1 if l1 else l2
        
        return dummy.next


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试正常合并
            l1 = ListNode(1)
            l1.next = ListNode(2)
            l1.next.next = ListNode(4)
            
            l2 = ListNode(1)
            l2.next = ListNode(3)
            l2.next.next = ListNode(4)
            
            merged = self.solution.mergeTwoLists(l1, l2)
            # 验证合并结果: 1->1->2->3->4->4
            self.assertEqual(merged.val, 1)
            self.assertEqual(merged.next.val, 1)
            self.assertEqual(merged.next.next.val, 2)
            self.assertEqual(merged.next.next.next.val, 3)
            self.assertEqual(merged.next.next.next.next.val, 4)
            self.assertEqual(merged.next.next.next.next.next.val, 4)
            self.assertIsNone(merged.next.next.next.next.next.next)
            
        def test_case2(self):
            # 测试空链表
            self.assertIsNone(self.solution.mergeTwoLists(None, None))
            
        def test_case3(self):
            # 测试一个链表为空
            l2 = ListNode(0)
            merged = self.solution.mergeTwoLists(None, l2)
            self.assertEqual(merged.val, 0)
            self.assertIsNone(merged.next)
            
    unittest.main()