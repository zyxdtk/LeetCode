"""
难度: medium
标签: 设计、字典树、哈希表、字符串

题目描述:
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """
        初始化前缀树数据结构
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入一个单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        搜索前缀树中是否存在完整的单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        检查前缀树中是否有以给定前缀开头的单词
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    import unittest
    
    class TestTrie(unittest.TestCase):
        def test_trie_operations(self):
            trie = Trie()
            trie.insert("apple")
            self.assertTrue(trie.search("apple"))
            self.assertFalse(trie.search("app"))
            self.assertTrue(trie.startsWith("app"))
            trie.insert("app")
            self.assertTrue(trie.search("app"))
            
    unittest.main()