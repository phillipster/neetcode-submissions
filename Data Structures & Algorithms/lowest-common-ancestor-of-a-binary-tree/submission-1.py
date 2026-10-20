# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_set, q_set = set([p]), set([q])
        def find_path(root, node, s):
            if not root:
                return False
            if root == node:
                return True
            if find_path(root.left, node, s) or find_path(root.right, node, s):
                s.add(root)
                return True
        find_path(root, p, p_set)
        find_path(root, q, q_set)
        print([i.val for i in p_set], [i.val for i in q_set])
        lowest_so_far, max_depth = root, 0
        def lowest(root, depth):
            nonlocal max_depth
            nonlocal lowest_so_far
            if not root:
                return
            if root in p_set and root in q_set and depth > max_depth:
                print(f"set: {root.val, max_depth}")
                lowest_so_far, max_depth = root, depth
            lowest(root.left, depth+1)
            lowest(root.right, depth+1)
        lowest(root, 0)
        return lowest_so_far
            