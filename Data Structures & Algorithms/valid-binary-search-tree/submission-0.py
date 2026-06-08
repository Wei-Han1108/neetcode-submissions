# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right) -> bool:
            if not node:
                return True
            if not left < node.val < right:
                return False
            # 向左走，左边界不变，右边界变当前node，因为向左走只要下个node即node.left小于上一个就行，不需要大于哪一个。
            # 而向右走，右边界不变原样传下去就行，因为向右走只要关心下一个值不要大于上一个val就行
            # 如果先向左走，再向右走，左边界就会是上一次向左走的时候，
            #    6
            #   /\
            #  4  8
            # /\ /\
            #3 5 7 9 检查5的时候，left是4，right是6
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))