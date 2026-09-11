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
            if not node:
                return
            m[node] = Node(node.val)
            for nei in node.neighbors:
                if nei in m:
                    m[node].neighbors.append(m[nei])
                else:
                    m[node].neighbors.append(dfs(nei))
            return m[node]
        
        m[node] = dfs(node)
        return m[node] if node in m else None
        
        
