class SetofPlates(object):

    def __init__(self, capacity):
        self.array = [[]]
        self.capacity = capacity

    def push(self, num):
        stack = self.array[-1]
        if len(stack) == self.capacity:
            self.array.append([num])
        else:
            stack.insert(0, num)

    def pop(self):
        if not self.array:
            return None
        stack = self.array[-1]
        while not stack:
            self.array.pop()
            stack = self.array[-1]
        temp = stack[0]
        del stack[0]
        if len(stack) == 0:
            self.array.pop()
        return temp

    def pop_at(self, index):
        if 0 <= index < len(self.array):
            stack = self.array[index]
            if not stack:
                return None
            temp = stack[0]
            del stack[0]
            return temp

import unittest

class Test(unittest.TestCase):

  def test_multi_stack(self):
    stack = SetofPlates(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
    self.assertEqual(stack.pop_at(1), 66)
    self.assertEqual(stack.pop_at(0), 33)
    self.assertEqual(stack.pop_at(1), 55)
    self.assertEqual(stack.pop_at(1), 44)
    self.assertEqual(stack.pop_at(1), None)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 77)
    self.assertEqual(stack.pop(), 22)
    self.assertEqual(stack.pop(), 11)
    self.assertEqual(stack.pop(), None)

if __name__ == "__main__":
  unittest.main()