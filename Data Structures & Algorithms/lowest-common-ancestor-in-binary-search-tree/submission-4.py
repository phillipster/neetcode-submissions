# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        curr = root
        while curr:
            if p.val <= curr.val <= q.val:
                return curr
            if curr.val < p.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr