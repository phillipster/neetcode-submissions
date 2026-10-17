class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        if self.freqs[val] > self.max_count:
            self.max_count = self.freqs[val]
        self.stacks[self.freqs[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.freqs[res] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()