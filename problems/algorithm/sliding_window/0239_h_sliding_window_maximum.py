"""
难度: hard
标签: 堆、滑动窗口、单调队列

题目描述:
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], k = 3
输出: [3,3,5,5,6,7] 
解释: 
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        if not nums:
            return []

        q = deque()
        res = []

        for i in range(len(nums)):
            # 移除超出窗口范围的元素
            if q and q[0] == i - k:
                q.popleft()

            # 维护单调递减队列
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            # 当窗口形成后开始记录结果
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            nums = [1, 3, -1, -3, 5, 3, 6, 7]
            k = 3
            self.assertEqual(
                self.solution.maxSlidingWindow(nums, k), [3, 3, 5, 5, 6, 7]
            )

        def test_case2(self):
            nums = [1, -1]
            k = 1
            self.assertEqual(self.solution.maxSlidingWindow(nums, k), [1, -1])

        def test_case3(self):
            nums = []
            k = 0
            self.assertEqual(self.solution.maxSlidingWindow(nums, k), [])

    unittest.main()
