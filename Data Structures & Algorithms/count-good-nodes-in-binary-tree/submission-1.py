# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root, num):
            if not root:
                return 0
            left = good(root.left, max(root.val, num))
            right = good(root.right, max(root.val, num))
            if root.val < num:
                return left + right
            else:
                return 1 + left + right
        
        return good(root, -float('inf'))