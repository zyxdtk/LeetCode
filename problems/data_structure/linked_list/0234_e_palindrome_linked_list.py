"""
难度: easy
标签: 链表、双指针

题目描述:
给你一个单链表的头节点 head，请你判断该链表是否为回文链表。如果是，返回 true；否则，返回 false。

示例:
输入: head = [1,2,2,1]
输出: true
输入: head = [1,2]
输出: false
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        使用快慢指针找到中点，反转后半部分链表，然后比较前后两部分
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not head or not head.next:
            return True

        # 找到中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # 比较前后两部分
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            # 测试回文链表: 1->2->2->1
            head = ListNode(1)
            head.next = ListNode(2)
            head.next.next = ListNode(2)
            head.next.next.next = ListNode(1)
            self.assertTrue(self.solution.isPalindrome(head))

        def test_case2(self):
            # 测试非回文链表: 1->2
            head = ListNode(1)
            head.next = ListNode(2)
            self.assertFalse(self.solution.isPalindrome(head))

        def test_case3(self):
            # 测试单节点链表
            head = ListNode(1)
            self.assertTrue(self.solution.isPalindrome(head))

        def test_case4(self):
            # 测试空链表
            self.assertTrue(self.solution.isPalindrome(None))

    unittest.main()
