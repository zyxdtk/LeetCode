"""
难度: medium
标签: 链表、数学

题目描述:
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字0之外，这两个数都不会以0开头。

示例:
输入: l1 = [2,4,3], l2 = [5,6,4]
输出: [7,0,8]
解释: 342 + 465 = 807
输入: l1 = [0], l2 = [0]
输出: [0]
输入: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        模拟加法运算过程
        时间复杂度: O(max(m,n))
        空间复杂度: O(max(m,n))
        """
        dummy = ListNode()  # 哨兵节点
        current = dummy
        carry = 0  # 进位
        
        while l1 or l2 or carry:
            # 计算当前位的和
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            # 更新进位和当前位的值
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # 移动指针
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 测试正常加法
            l1 = ListNode(2)
            l1.next = ListNode(4)
            l1.next.next = ListNode(3)
            
            l2 = ListNode(5)
            l2.next = ListNode(6)
            l2.next.next = ListNode(4)
            
            result = self.solution.addTwoNumbers(l1, l2)
            # 验证结果: 7->0->8
            self.assertEqual(result.val, 7)
            self.assertEqual(result.next.val, 0)
            self.assertEqual(result.next.next.val, 8)
            self.assertIsNone(result.next.next.next)
            
        def test_case2(self):
            # 测试有进位的情况
            l1 = ListNode(9)
            l1.next = ListNode(9)
            l1.next.next = ListNode(9)
            
            l2 = ListNode(1)
            
            result = self.solution.addTwoNumbers(l1, l2)
            # 验证结果: 0->0->0->1
            self.assertEqual(result.val, 0)
            self.assertEqual(result.next.val, 0)
            self.assertEqual(result.next.next.val, 0)
            self.assertEqual(result.next.next.next.val, 1)
            self.assertIsNone(result.next.next.next.next)
            
        def test_case3(self):
            # 测试不同长度链表
            l1 = ListNode(1)
            
            l2 = ListNode(9)
            l2.next = ListNode(9)
            
            result = self.solution.addTwoNumbers(l1, l2)
            # 验证结果: 0->0->1
            self.assertEqual(result.val, 0)
            self.assertEqual(result.next.val, 0)
            self.assertEqual(result.next.next.val, 1)
            self.assertIsNone(result.next.next.next)
            
    unittest.main()