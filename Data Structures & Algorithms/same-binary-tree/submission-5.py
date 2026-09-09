# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            c1 = q1.popleft()
            c2 = q2.popleft()
            if not (c1 or c2):
                continue
            if (bool(c1) ^ bool(c2)) or (c1.val != c2.val):
                return False
            q1.append(c1.left)
            q1.append(c1.right)
            q2.append(c2.left)
            q2.append(c2.right)
        if q1 or q2:
            return False
        return True
        
            