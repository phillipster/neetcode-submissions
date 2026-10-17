# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s, res = [root], []
        while s:
            curr = s.pop()
            res.append(curr.val)
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)
        return res
