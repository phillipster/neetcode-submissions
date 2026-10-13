# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arch_sum = 0
        global_max = -inf

        def dfs(root):
            if not root:
                return 0
            left_gain = dfs(root.left)
            right_gain = dfs(root.right)
            arch_sum = root.val + max(0, left_gain) + max(0, right_gain)
            nonlocal global_max
            global_max = max(global_max, arch_sum)
            return root.val + max(0, left_gain, right_gain)
        
        dfs(root)
        return global_max

