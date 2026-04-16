class MinStack:

    def __init__(self):
        self.last = -1
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.last == len(self.stack) - 1:
            self.stack.append(val)
            self.last += 1
            if len(self.minStack) == 0:
                self.minStack.append(val)
            else:
                self.minStack.append(val if val < self.minStack[-1] else self.minStack[-1])
        else:
            self.last += 1
            self.stack[self.last] = val
            if self.last == 0:
                self.minStack[self.last] = val
            else:
                self.minStack[self.last] = val if val < self.minStack[self.last-1] else self.minStack[self.last-1]

        

    def pop(self) -> None:
        self.last -= 1
        

    def top(self) -> int:
        return self.stack[self.last]
        

    def getMin(self) -> int:
        return self.minStack[self.last]
        
