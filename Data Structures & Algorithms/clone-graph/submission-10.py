"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        m = {}
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            if cur not in m:
                m[cur] = Node(cur.val)
            for nei in cur.neighbors:
                if nei in m:
                    m[cur].neighbors.append(m[nei])
                else:
                    m[nei] = Node(nei.val)
                    m[cur].neighbors.append(m[nei])
                    q.append(nei)
        return m[node]
