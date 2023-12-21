import unittest

class Stack:
    def __init__(self, size) -> None:
        self.size = size
        self.stack = [0 for _ in range(size)]
        self.top = -1

    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.size - 1
    
    def getSize(self) -> int:
        return self.size
    
    def push(self, v):
        if not self.isFull():
            self.top +=1
            self.stack[self.top] = v
        else:
            print("Stack Overflow!")
        
    def pop(self):
        if not self.isEmpty():
            val = self.stack[self.top]
            self.top -=1
            return val
        else:
            print ("Stack Underflow!")

    def getTop(self):
        return self.stack[self.top]


class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.isEmpty())

    def test_is_empty(self):
        stack = Stack(3)
        self.assertTrue(stack.isEmpty())
        stack.push(10)
        self.assertFalse(stack.isEmpty())
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_is_full(self):
        stack = Stack(2)
        self.assertFalse(stack.isFull())
        stack.push(5)
        stack.push(10)
        self.assertTrue(stack.isFull())
        stack.pop()
        self.assertFalse(stack.isFull())

    def test_get_top(self):
        stack = Stack(4)
        stack.push(15)
        stack.push(25)
        stack.push(35)

        self.assertEqual(stack.getTop(), 35)
        stack.pop()
        self.assertEqual(stack.getTop(), 25)

    def test_stack_overflow(self):
        stack = Stack(2)
        stack.push(5)
        stack.push(10)
        with self.assertRaises(Exception):
            stack.push(15)

    def test_stack_underflow(self):
        stack = Stack(3)
        with self.assertRaises(Exception):
            stack.pop()

if __name__ == '__main__':
    unittest.main()
