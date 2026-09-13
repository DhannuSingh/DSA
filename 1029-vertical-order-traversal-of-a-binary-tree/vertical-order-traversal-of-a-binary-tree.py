# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> list:
        nodes = []

        # DFS traversal to collect (x, y, val) for every node
        def dfs(node, x, y):
            if not node:
                return
            nodes.append((x, y, node.val))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)

        # Sort nodes by: x ascending, y ascending, val ascending
        nodes.sort(key=lambda item: (item[0], item[1], item[2]))

        # Group values by column x
        result = []
        prev_x = None

        for x, y, val in nodes:
            if x != prev_x:
                result.append([])
                prev_x = x
            result[-1].append(val)

        return result