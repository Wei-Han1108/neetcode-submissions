# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # low high 限制每个节点，刷新low high 用node，左节点low是，high是父节点
        # 右节点low是父节点，high不刷新

        def dfs(node, low, high) -> bool:
            if node is None:
                return True
            # left right cant be none
            if not (low < node.val < high):
                return False          
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))