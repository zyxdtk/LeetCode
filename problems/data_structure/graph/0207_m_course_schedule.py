"""
难度: medium
标签: 深度优先搜索、广度优先搜索、图、拓扑排序

题目描述:
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1。
在选修某些课程之前需要一些先修课程。先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [a, b]，表示如果要学习课程 a 必须先学习课程 b。
请你判断是否可能完成所有课程的学习？如果可以，返回 true；否则，返回 false。

示例:
输入: numCourses = 2, prerequisites = [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
输入: numCourses = 2, prerequisites = [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0；并且学习课程 0 之前，你需要完成课程 1。这是不可能的。
"""

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        拓扑排序解法
        时间复杂度: O(V+E)
        空间复杂度: O(V+E)
        """
        # 构建邻接表和入度数组
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        # 初始化队列
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 拓扑排序
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses


if __name__ == "__main__":
    import unittest
    
    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()
            
        def test_case1(self):
            numCourses = 2
            prerequisites = [[1,0]]
            self.assertTrue(self.solution.canFinish(numCourses, prerequisites))
            
        def test_case2(self):
            numCourses = 2
            prerequisites = [[1,0],[0,1]]
            self.assertFalse(self.solution.canFinish(numCourses, prerequisites))
            
    unittest.main()