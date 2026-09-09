"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS
        if not node: 
            return None
        visited = {}
        visited[node] = Node(node.val)
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    q.append(n)
                visited[cur].neighbors.append(visited[n])

        return visited[node]

    """ DFS solution:
        if not node:
            return None
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            result = Node(node.val)
            visited[node] = result
            for n in node.neighbors:
                result.neighbors.append(dfs(n))
            return result

        return dfs(node)
    """
        