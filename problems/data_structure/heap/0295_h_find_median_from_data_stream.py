"""
难度: hard
标签: 设计、双指针、数据流、排序、堆(优先队列)

题目描述:
设计一个支持以下两种操作的数据结构：
1. void addNum(int num) - 从数据流中添加一个整数到数据结构中。
2. double findMedian() - 返回目前所有元素的中位数。

示例:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        初始化数据结构。
        使用两个堆：最大堆存储较小一半数，最小堆存储较大一半数
        """
        self.max_heap = []  # 存储较小一半，使用负数模拟最大堆
        self.min_heap = []  # 存储较大一半

    def addNum(self, num: int) -> None:
        # 先加入最大堆
        heapq.heappush(self.max_heap, -num)
        # 将最大堆的最大值移到最小堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # 保持堆的大小平衡
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == "__main__":
    import unittest
    
    class TestMedianFinder(unittest.TestCase):
        def test_median_finder(self):
            finder = MedianFinder()
            finder.addNum(1)
            finder.addNum(2)
            self.assertEqual(finder.findMedian(), 1.5)
            finder.addNum(3)
            self.assertEqual(finder.findMedian(), 2.0)
            
    unittest.main()