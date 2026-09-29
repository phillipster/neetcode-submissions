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
        m = {None:None}
        cur = head
        prev = None
        while cur:
            m[cur] = Node(cur.val)
            if prev:
                m[prev].next = m[cur]
            prev = cur
            cur = cur.next
        cur = head
        while cur:
            m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]