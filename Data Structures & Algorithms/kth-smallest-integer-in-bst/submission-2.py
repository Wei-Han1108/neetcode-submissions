# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inOrder可以从小到大遍历
        # 优化：想要遍历到第k个就停止
        self.count = 0
        self.res = None
        def dfs(node):
            if node is None or self.res is not None:
                return 
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res
