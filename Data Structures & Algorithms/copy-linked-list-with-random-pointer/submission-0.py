from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {None : None}
        q = deque()
        cursor = head
        while cursor:
            m[cursor] = Node(cursor.val)
            cursor = cursor.next
        cursor = head
        while cursor:
            m[cursor].next = m[cursor.next]
            m[cursor].random = m[cursor.random]
            cursor = cursor.next
        return m[head]

        