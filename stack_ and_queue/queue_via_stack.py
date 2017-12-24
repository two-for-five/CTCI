
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def remove(self):
        if not self.stack1 and not self.stack2:
            return None
        elif not self.stack2:
            while self.stack1:
                self.stack2.insert(0, self.stack1.pop(0))
        return self.stack2.pop(0)

    def add(self, num):
        self.stack1.insert(0, num)

import unittest

class Test(unittest.TestCase):
  def test_queue_via_stacks(self):
      queue = MyQueue()
      queue.add(11)
      queue.add(22)
      queue.add(33)
      self.assertEqual(queue.remove(), 11)
      queue.add(44)
      queue.add(55)
      queue.add(66)
      self.assertEqual(queue.remove(), 22)
      self.assertEqual(queue.remove(), 33)
      self.assertEqual(queue.remove(), 44)
      self.assertEqual(queue.remove(), 55)
      queue.add(77)
      self.assertEqual(queue.remove(), 66)
      self.assertEqual(queue.remove(), 77)
      self.assertEqual(queue.remove(), None)