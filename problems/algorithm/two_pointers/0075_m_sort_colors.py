"""
难度: medium
标签: 数组、双指针、排序

题目描述:
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。

示例:
输入: nums = [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        荷兰国旗问题解法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        p0 = 0  # 0的右边界
        p2 = len(nums) - 1  # 2的左边界
        curr = 0
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            nums = [2,0,2,1,1,0]
            expected = [0,0,1,1,2,2]
            self.solution.sortColors(nums)
            self.assertEqual(nums, expected)
            
        def test_case2(self):
            nums = [2,0,1]
            expected = [0,1,2]
            self.solution.sortColors(nums)
            self.assertEqual(nums, expected)
            
    unittest.main()