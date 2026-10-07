# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def help(root, maxval):
            if not root:
                return 0
            l = help(root.left, max(maxval, root.val))
            r = help(root.right, max(maxval, root.val))
            if root.val >= maxval:
                l += 1
            return l + r
        
        return help(root, -inf)