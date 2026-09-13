# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return (0, None)
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            # If both subtrees have equal max depth, current node is the candidate LCA
            if left_depth == right_depth:
                return (left_depth + 1, node)
            
            # Left subtree is deeper
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            
            # Right subtree is deeper
            return (right_depth + 1, right_lca)

        return dfs(root)[1]