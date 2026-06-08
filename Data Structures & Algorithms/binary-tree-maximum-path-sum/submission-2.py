# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # current_path和sum比较
        self.sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            current_path = node.val + left_gain + right_gain
            self.sum = max(self.sum, current_path)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return(self.sum)
        