class MyStack:

    def __init__(self):
        self.data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        for i in range(len(self.data)-1):
            self.data.append(self.data.popleft())
        return self.data.popleft()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()