# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 从下到上每一个节点左右节点的贡献值，负为0
        self.sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_con = max(0, dfs(node.left))
            right_con = max(0, dfs(node.right))
            current_path = node.val + +left_con+ right_con
            self.sum = max(self.sum, current_path)
            return node.val + max(left_con, right_con)
        dfs(root)
        return self.sum

