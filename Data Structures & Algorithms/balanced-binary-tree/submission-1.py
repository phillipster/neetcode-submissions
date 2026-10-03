# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(root):
            if not root:
                return 0, True
            left_height, left_balanced = bal(root.left)
            right_height, right_balanced = bal(root.right)
            print(f"node: {root.val}, left_height: {left_height}, right_height: {right_height}")
            return 1 + max(left_height, right_height), left_balanced \
            and right_balanced and abs(left_height-right_height) <= 1

        return bal(root)[1]

