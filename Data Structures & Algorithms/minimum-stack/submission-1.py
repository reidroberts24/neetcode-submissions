class MinStack:
    def __init__(self):
        self.stack = []
        self.min_idx = []

    def push(self, val: int) -> None:
        if not self.min_idx or val < self.stack[self.min_idx[-1]]:
            self.min_idx.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_idx[-1] == len(self.stack) - 1:
            self.min_idx.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_idx[-1]]