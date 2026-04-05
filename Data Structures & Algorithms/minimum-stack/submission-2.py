class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31

    def push(self, val: int) -> None:
        self.min = min(self.min,val)
        self.stack.append((val,self.min))

    def pop(self) -> None:
        top_element = self.stack.pop()
        if len(self.stack) == 0:
            self.min = 2**31
        elif top_element[1] == self.min:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
