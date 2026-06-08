# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 好点需要比路径中的所有的点大,也就是比最近的好点大，也就是比路径上最大的值大
        # path记录路径上所有的值
        # 因为右子树path不同，so需要浅复制path
        path = []
        self.good = 0
        def dfs(node, path):
            if node is None:
                return 
            path.append(node.val)
            if node.val >= max(path):
                self.good += 1
            dfs(node.left, path[:])
            dfs(node.right, path[:])
        dfs(root, [])
        return self.good

            
        