# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 遍历树做成string
        if not root:
             return ''
        res = []
        que = deque([root])
        while que:
            node = que.popleft()           
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                res.append('null')
        return ','.join(res)

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        value = data.split(',')
        root = TreeNode(int(value[0]))
        que = deque([root])
        i = 1
        while que:
            node = que.popleft()
            if value[i] != 'null':
                node.left = TreeNode(int(value[i]))
                que.append(node.left)
            i += 1
            if value[i] != 'null':
                node.right = TreeNode(int(value[i]))
                que.append(node.right)
            i += 1
        return root
