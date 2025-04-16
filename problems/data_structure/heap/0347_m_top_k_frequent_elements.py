"""
难度: medium
标签: 数组、哈希表、分治、桶排序、计数、排序、堆(优先队列)、快速选择

题目描述:
给你一个整数数组 nums 和一个整数 k，请你返回其中出现频率前 k 高的元素。

示例:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
输入: nums = [1], k = 1
输出: [1]
"""

import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        使用最小堆实现
        时间复杂度: O(n log k)
        空间复杂度: O(n)
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        """
        桶排序实现
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        count = Counter(nums)
        max_freq = max(count.values())
        
        # 创建桶
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 从高频率到低频率收集结果
        result = []
        for i in range(max_freq, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                break
                
        return result[:k]


if __name__ == "__main__":
    import unittest
    from typing import List
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [1,1,1,2,2,3]
            k = 2
            self.assertCountEqual(self.solution.topKFrequent(nums, k), [1,2])
            
        def test_case2(self):
            nums = [1]
            k = 1
            self.assertEqual(self.solution.topKFrequent(nums, k), [1])
            
    unittest.main()