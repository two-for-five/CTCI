class stack(object):
    def __init__(self):
        self.reg_stack = []
        self.min_stack = []

    def push(self, num):
        self.reg_stack.insert(0, num)
        if not self.min_stack:
            self.min_stack.insert(0, num)
        else:
            if num < self.min_stack[0]:
                self.min_stack.insert(0, num)
            else:
                self.min_stack.insert(0, self.min_stack[0])

    def pop(self):
        if not self.reg_stack:
            return None
        temp = self.reg_stack[0]
        del self.reg_stack[0]
        del self.min_stack[0]
        return temp

    def min(self):
        return self.min_stack[0]
test = stack()
test.push(1)
test.push(2)
test.push(3)
print(test.min())
test.push(0)
print(test.min())
test.pop()
print(test.min())