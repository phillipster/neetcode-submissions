# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_height(root):
            if not root:
                return 0
            return 1 + max(max_height(root.left), max_height(root.right))

        def dfs(root):
            if not root:
                return 0
            left_max = max_height(root.left)
            right_max = max_height(root.right)
            diameter = left_max + right_max
            return max(diameter, dfs(root.left), dfs(root.right))

        return dfs(root)