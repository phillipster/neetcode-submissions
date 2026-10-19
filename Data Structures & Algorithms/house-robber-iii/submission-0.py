# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        m = {None : 0}
        def dfs(root):
            if root in m:
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if not (root.left or root.right):
                m[root] = root.val
            grandchildren = 0
            children = 0
            if root.left:
                children += m[root.left]
                grandchildren += m[root.left.left] + m[root.left.right]
            if root.right:
                children += m[root.right]
                grandchildren += m[root.right.left] + m[root.right.right]
            m[root] = max(children, root.val + grandchildren)

        dfs(root)
        return m[root]

        
        