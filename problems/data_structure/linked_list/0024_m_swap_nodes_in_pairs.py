"""
难度: medium
标签: 链表、递归

题目描述:
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
输入: head = [1,2,3,4]
输出: [2,1,4,3]
输入: head = []
输出: []
输入: head = [1]
输出: [1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代法实现两两交换节点
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        dummy = ListNode(0, head)  # 哨兵节点
        prev = dummy
        
        while prev.next and prev.next.next:
            # 获取当前要交换的两个节点
            first = prev.next
            second = first.next
            
            # 执行交换操作
            prev.next = second
            first.next = second.next
            second.next = first
            
            # 移动prev指针
            prev = first
            
        return dummy.next


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试偶数个节点交换
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            
            result = self.solution.swapPairs(head)
            # 验证结果: 2->1->4->3
            self.assertEqual(result.val, 2)
            self.assertEqual(result.next.val, 1)
            self.assertEqual(result.next.next.val, 4)
            self.assertEqual(result.next.next.next.val, 3)
            self.assertIsNone(result.next.next.next.next)
            
        def test_case2(self):
            # 测试奇数个节点交换
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            
            result = self.solution.swapPairs(head)
            # 验证结果: 2->1->3
            self.assertEqual(result.val, 2)
            self.assertEqual(result.next.val, 1)
            self.assertEqual(result.next.next.val, 3)
            self.assertIsNone(result.next.next.next)
            
        def test_case3(self):
            # 测试单个节点
            head = ListNode(1)
            result = self.solution.swapPairs(head)
            self.assertEqual(result.val, 1)
            self.assertIsNone(result.next)
            
        def test_case4(self):
            # 测试空链表
            self.assertIsNone(self.solution.swapPairs(None))
            
    unittest.main()