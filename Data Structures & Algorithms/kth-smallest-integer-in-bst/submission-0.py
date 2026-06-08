# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 二叉搜索树先排序乘数组 然后找到第k小的
        # 二叉搜索树中序遍历（左中右）就是从小到大排序
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
                
        dfs(root)
        return arr[k-1]
