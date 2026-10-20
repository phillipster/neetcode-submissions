# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        right_view = []
        while q:
            level = 0
            prev = None
            for i in range(len(q)):
                prev = q.popleft()
                if prev.left:
                    q.append(prev.left)
                if prev.right:
                    q.append(prev.right)
            if prev:
                right_view.append(prev.val)
        return right_view
