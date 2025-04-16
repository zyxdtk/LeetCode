"""
难度: medium
标签: 栈、设计

题目描述:
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3
minStack.pop();
minStack.top();      --> 返回 0
minStack.getMin();   --> 返回 -2
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    import unittest
    
    class TestMinStack(unittest.TestCase):
        def test_min_stack(self):
            min_stack = MinStack()
            min_stack.push(-2)
            min_stack.push(0)
            min_stack.push(-3)
            self.assertEqual(min_stack.getMin(), -3)
            min_stack.pop()
            self.assertEqual(min_stack.top(), 0)
            self.assertEqual(min_stack.getMin(), -2)
            
    unittest.main()