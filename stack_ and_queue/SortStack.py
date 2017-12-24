
class min_stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop(0)

    def push(self, num):
        self.stack.insert(0, num)

    def peek(self):
        if self.stack:
            return self.stack[0]
        return None

    def sort(self):
        temp_stack = []
        while self.stack:
            num = self.stack.pop(0)
            if not temp_stack:
                temp_stack.append(num)
            else:
                if num >= temp_stack[0]:
                    temp_stack.insert(0, num)
                else:
                    while temp_stack and temp_stack[0] > num:
                        self.stack.insert(0, temp_stack.pop(0))
                    temp_stack.insert(0, num)
        while temp_stack:
            self.stack.insert(0, temp_stack.pop(0))



import unittest

class Test(unittest.TestCase):
    def test_sort_stack(self):
        stack = min_stack()
        stack.push(10)
        stack.push(30)
        stack.push(70)
        stack.push(40)
        stack.push(80)
        stack.push(20)
        stack.push(90)
        stack.push(50)
        stack.push(60)
        stack.sort()
        self.assertEqual(stack.peek(), 10)
        stack.pop()
        self.assertEqual(stack.peek(), 20)


if __name__ == "__main__":
    unittest.main()