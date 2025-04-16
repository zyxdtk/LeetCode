"""
难度: easy
标签: 链表、双指针

题目描述:
给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null。
题目数据保证整个链式结构中不存在环。
注意，函数返回结果后，链表必须保持其原始结构。

示例:
输入: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出: Intersected at '8'
解释: 相交节点的值为 8 (注意，如果两个链表相交则不能为 0)。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针法：让两个指针分别遍历两个链表，当到达链表末尾时切换到另一个链表头部继续遍历
        如果两链表相交，则会在交点相遇；如果不相交，则最终都会指向None
        """
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            # 构造相交链表
            # listA = [4,1,8,4,5]
            # listB = [5,6,1,8,4,5]
            # 相交于节点8
            common = ListNode(8)
            common.next = ListNode(4)
            common.next.next = ListNode(5)

            headA = ListNode(4)
            headA.next = ListNode(1)
            headA.next.next = common

            headB = ListNode(5)
            headB.next = ListNode(6)
            headB.next.next = ListNode(1)
            headB.next.next.next = common

            result = self.solution.getIntersectionNode(headA, headB)
            self.assertEqual(result, common)

        def test_case2(self):
            # listA = [2,6,4]
            # listB = [1,5]
            # 不相交
            headA = ListNode(2)
            headA.next = ListNode(6)
            headA.next.next = ListNode(4)

            headB = ListNode(1)
            headB.next = ListNode(5)

            result = self.solution.getIntersectionNode(headA, headB)
            self.assertIsNone(result)

    unittest.main()
