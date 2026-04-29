class MyQueue:

    def __init__(self):
        self.q = [] # [1, 2, 3]
        self.reversed_q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        if not self.reversed_q:
            while self.q:
                self.reversed_q.append(self.q.pop())
        return self.reversed_q.pop()


    def peek(self) -> int:
        if not self.reversed_q:
            while self.q:
                self.reversed_q.append(self.q.pop())
        return self.reversed_q[-1]

    def empty(self) -> bool:
        return max(len(self.reversed_q), len(self.q)) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()