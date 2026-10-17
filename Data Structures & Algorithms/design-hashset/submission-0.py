class MyHashSet:

    def __init__(self):
        self.data = [[] for i in range(128)]
        self.capacity = 128
        self.size = 0

    def add(self, key: int) -> None:
        addr = key % self.capacity
        if key not in self.data[addr]:
            self.data[addr].append(key)
            self.size += 1

    def remove(self, key: int) -> None:
        addr = key % self.capacity
        if key not in self.data[addr]:
            return
        self.data[addr].remove(key)

    def contains(self, key: int) -> bool:
        addr = key % self.capacity
        return key in self.data[addr]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)