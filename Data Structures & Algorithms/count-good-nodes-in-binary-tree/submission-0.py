# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 暴力 找出到每个节点的路径
        # 定义一个列表res
        good = [0]
        # 列表中储存每个节点的路径列表
        # 本节点的路径是上面节点路径+本节点
        # 如果上面节点是好，本节点大于等于上面节点，本节点好
        # 如果上面节点是坏，路径中上一个好节点，比较大小，本节点大于等于这个好，就是好
        # 合起来就是，找本路径上一个好节点，比较大小，大于等于它就好，否则就坏
        # 而且其实最近的好节点值就是路径中最大的值
        def dfs(node, path):
            if node is None:
                return
            if not path or node.val >= max(path):
                path.append(node.val)
                good[0] += 1
            dfs(node.left, path[:])
            dfs(node.right, path[:])
        
        dfs(root,[])
        return good[0]


        