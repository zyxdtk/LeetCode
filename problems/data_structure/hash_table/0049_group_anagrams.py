"""
难度: medium
标签: 数组、哈希表、字符串

题目描述:
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
            expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
            result = self.solution.groupAnagrams(strs)
            # 对结果和预期都进行排序，确保顺序不影响比较
            sorted_result = [
                sorted(group) for group in sorted(result, key=lambda x: len(x))
            ]
            sorted_expected = [
                sorted(group) for group in sorted(expected, key=lambda x: len(x))
            ]
            self.assertEqual(sorted_result, sorted_expected)

        def test_case2(self):
            strs = [""]
            self.assertEqual(self.solution.groupAnagrams(strs), [[""]])

        def test_case3(self):
            strs = ["a"]
            self.assertEqual(self.solution.groupAnagrams(strs), [["a"]])

    unittest.main()
