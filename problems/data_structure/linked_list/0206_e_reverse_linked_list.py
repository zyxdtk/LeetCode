"""
难度: easy
标签: 链表

题目描述:
给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

示例:
输入: head = [1,2,3,4,5]
输出: [5,4,3,2,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代法反转链表
        使用三个指针：prev, curr, next
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # 临时保存下一个节点
            curr.next = prev  # 反转指针方向
            prev = curr  # 移动prev指针
            curr = next_node  # 移动curr指针

        return prev  # 最后prev指向新的头节点


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            # 测试用例1: 1->2->3->4->5
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(3)
            head.next.next.next = ListNode(4)
            head.next.next.next.next = ListNode(5)

            reversed_head = self.solution.reverseList(head)
            # 验证反转后的链表: 5->4->3->2->1
            self.assertEqual(reversed_head.val, 5)
            self.assertEqual(reversed_head.next.val, 4)
            self.assertEqual(reversed_head.next.next.val, 3)
            self.assertEqual(reversed_head.next.next.next.val, 2)
            self.assertEqual(reversed_head.next.next.next.next.val, 1)
            self.assertIsNone(reversed_head.next.next.next.next.next)

        def test_case2(self):
            # 测试用例2: 空链表
            head = None
            reversed_head = self.solution.reverseList(head)
            self.assertIsNone(reversed_head)

        def test_case3(self):
            # 测试用例3: 单个节点
            head = ListNode(1)
            reversed_head = self.solution.reverseList(head)
            self.assertEqual(reversed_head.val, 1)
            self.assertIsNone(reversed_head.next)

    unittest.main()
