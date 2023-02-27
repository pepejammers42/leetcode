class MinStack:

    def __init__(self):
        self.s = []
        self.small = 0

    def push(self, val: int) -> None:
        if len(self.s) == 0 or val < self.small:
            self.small = val
        self.s.append((val, self.small)) 

    def pop(self) -> None:
        self.s.pop();        
        self.small = self.s[-1][1]

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()