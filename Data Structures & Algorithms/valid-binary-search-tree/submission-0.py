# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, l, r):
            if not root:
                return True
            left = valid(root.left, l, root.val)
            right = valid(root.right, root.val, r)
            return left and right and root.val > l and root.val < r
        return valid(root, -inf, inf)
            