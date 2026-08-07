# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes = {}
        
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                nodes[node.val] = (parent, depth)
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)
        
        if x in nodes and y in nodes:
            parent_x, depth_x = nodes[x]
            parent_y, depth_y = nodes[y]
            return depth_x == depth_y and parent_x != parent_y
        return False
