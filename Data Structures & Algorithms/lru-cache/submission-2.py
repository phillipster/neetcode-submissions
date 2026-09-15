from collections import deque

class LRUCache:

    class Node:
        def __init__(self, key = None, val = None, prev = None, next = None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.m = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _evict_last(self):
        sec_to_last = self.tail.prev.prev
        sec_to_last.next = self.tail
        self.tail.prev = sec_to_last

    def _move_to_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.m:
            self._move_to_front(self.m[key])
            return self.m[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].val = value
            self._move_to_front(self.m[key])
            return
        if self.n == self.capacity:
            self.n -= 1
            del self.m[self.tail.prev.key]
            self._evict_last()
        node = self.Node(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.m[key] = node
        self.n += 1
        
            

        
