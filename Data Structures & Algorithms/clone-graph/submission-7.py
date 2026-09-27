"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = {}
        def dfs(node):
            if node in m:
                return m[node]
            m[node] = Node(node.val)
            for nei in node.neighbors:
                if nei in m:
                    m[node].neighbors.append(m[nei])
                else:
                    m[node].neighbors.append(dfs(nei))
            return m[node]
        return None if not node else dfs(node)