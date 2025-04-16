"""
难度: hard
标签: 链表、分治、堆(优先队列)

题目描述:
给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例:
输入: lists = [[1,4,5],[1,3,4],[2,6]]
输出: [1,1,2,3,4,4,5,6]
输入: lists = []
输出: []
输入: lists = [[]]
输出: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        使用最小堆合并K个有序链表
        时间复杂度: O(N log k) N是所有节点总数，k是链表数量
        空间复杂度: O(k)
        """
        # 创建最小堆
        min_heap = []
        # 初始化堆，存储每个链表的头节点
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy = ListNode(0)
        curr = dummy
        
        # 不断从堆中取出最小节点
        while min_heap:
            val, i = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next
            # 如果该链表还有剩余节点，继续加入堆中
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        return dummy.next


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            # 构建测试链表
            list1 = ListNode(1)
            list1.next = ListNode(4)
            list1.next.next = ListNode(5)
            
            list2 = ListNode(1)
            list2.next = ListNode(3)
            list2.next.next = ListNode(4)
            
            list3 = ListNode(2)
            list3.next = ListNode(6)
            
            lists = [list1, list2, list3]
            result = self.solution.mergeKLists(lists)
            
            # 验证结果: 1->1->2->3->4->4->5->6
            expected = [1,1,2,3,4,4,5,6]
            curr = result
            for num in expected:
                self.assertEqual(curr.val, num)
                curr = curr.next
            self.assertIsNone(curr)
            
        def test_case2(self):
            # 测试空列表
            self.assertIsNone(self.solution.mergeKLists([]))
            
        def test_case3(self):
            # 测试包含空链表的情况
            list1 = ListNode(1)
            list1.next = ListNode(2)
            list2 = None
            list3 = ListNode(3)
            
            lists = [list1, list2, list3]
            result = self.solution.mergeKLists(lists)
            
            # 验证结果: 1->2->3
            expected = [1,2,3]
            curr = result
            for num in expected:
                self.assertEqual(curr.val, num)
                curr = curr.next
            self.assertIsNone(curr)
            
    unittest.main()