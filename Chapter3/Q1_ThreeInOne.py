class ThreeStack:
    def __init__(self):
        self.index = [0, 0, 0]
        self.stack = []
        self.size = 0

    def __str__(self):
        string = str(self.stack)
        return string

    def add(self, stack_num, value):
        index = 3 * self.index[stack_num] + stack_num
        if index + 1 > self.size:
            to_append = [None] * (index + 1 - self.size)
            self.stack.extend(to_append)
            self.size = index + 1
        self.stack[index] = value
        self.index[stack_num] += 1

    def is_empty(self, stack_num):
        return self.index[stack_num] == 0

    def peek(self, stack_num):
        if not self.is_empty(stack_num):
            index =  3 * (self.index[stack_num] - 1) + stack_num
            return self.stack[index]
        else:
            return None

    def pop(self, stack_num):
        if self.index[stack_num] > 0:
            index = 3 * (self.index[stack_num] - 1) + stack_num
            value = self.stack[index]
            self.stack[index] = None  # Empty that part of the stack
            self.index[stack_num] -= 1
            return value
        else:
            return None

# Main code
stack = ThreeStack()

for i in range(50):
    stack.add(2, i)

print(stack)

for i in range(25):
    stack.add(1, i)

print(stack)

for i in range(25):
    stack.pop(2)

print(stack)

print(stack.peek(2))

print(stack.is_empty(0))

