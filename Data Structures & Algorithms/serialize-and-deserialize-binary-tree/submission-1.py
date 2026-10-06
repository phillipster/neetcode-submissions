# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(root):
            if root:
                result.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                result.append('Null')
        dfs(root)
        return ','.join(result)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        def dfs(i):
            if data[i] != 'Null':
                root = TreeNode(int(data[i]))
                left_node, next_index = dfs(i+1)
                right_node, right_index = dfs(next_index)
                root.left = left_node
                root.right = right_node
                return root, right_index
            else:
                return None, i+1
        return dfs(0)[0]
