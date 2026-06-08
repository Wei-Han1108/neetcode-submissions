# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs中
        # 遍历每一个节点，如果左孩子没有，就返回；如果右孩子没有，要左孩子<本节点；
        # 一旦左右孩子都有，就要左孩子<本节点<右孩子，一旦某个是None，就return。
        # 一旦不满足，返回false
        # 遍历到最后，返回true

        # 返回左右子树bool的and
        # 必须限制本节点在low和high之间，对左子树，high是父节点，low是路径上如果当过右子树的路径上的最大值
        # 对右子树low是父节点的值，high是如果当过左子树的最小值
        def dfs(node, low, high):
            if node is None:
                return True # 如果左子树是True还不够，整体True是左右子树的AND
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float('-inf'), float('inf'))
    










