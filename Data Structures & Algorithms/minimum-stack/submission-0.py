class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val: int | None = None
        

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_val))

        if self.min_val is None or val <= self.min_val:
            self.min_val = val
        

    def pop(self) -> None:
        res, last_min = self.stack[-1]
        self.stack.pop()
        self.min_val = last_min
        return res
        

    def top(self) -> int:
        res, last_min = self.stack[-1]
        return res
        

    def getMin(self) -> int:
        return self.min_val

        
