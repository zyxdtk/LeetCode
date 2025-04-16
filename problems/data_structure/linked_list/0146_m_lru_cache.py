"""
难度: medium
标签: 设计、哈希表、链表、双向链表

题目描述:
请你设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。
实现 LRUCache 类：
- LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
- int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1
- void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value；
  如果不存在，则向缓存中插入该组 key-value。
  如果插入操作导致关键字数量超过 capacity，则应该逐出最久未使用的关键字。

示例:
输入:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出:
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                del self.cache[removed.key]
                self.size -= 1

    def addToHead(self, node: DLinkedNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkedNode) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self) -> DLinkedNode:
        node = self.tail.prev
        self.removeNode(node)
        return node


if __name__ == "__main__":
    import unittest

    class TestLRUCache(unittest.TestCase):
        def test_lru_cache(self):
            lru = LRUCache(2)
            lru.put(1, 1)
            lru.put(2, 2)
            self.assertEqual(lru.get(1), 1)
            lru.put(3, 3)  # 2被淘汰
            self.assertEqual(lru.get(2), -1)
            lru.put(4, 4)  # 1被淘汰
            self.assertEqual(lru.get(1), -1)
            self.assertEqual(lru.get(3), 3)
            self.assertEqual(lru.get(4), 4)

    unittest.main()
