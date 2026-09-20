# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_count = 0
        work = []
        def dfs(node, level):
            if not node:
                return
            work.append((node.val, level))
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        res = [list() for i in range(len(work))]
        for value, level in work:
            res[level].append(value)
        while len(res[-1]) == 0:
            res.pop()
        return res

