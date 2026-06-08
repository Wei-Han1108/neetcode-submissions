# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 前序第一个是根节点
        in_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(pre_left, pre_right, in_left, in_right):
            # 如果相等的话，还有一个节点没处理
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            in_root_idx = in_map[root_val]
            left_size = in_root_idx - in_left
            # pre_left 要加一作为起点，因为root已经用过了0
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, in_root_idx + 1, in_right)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

