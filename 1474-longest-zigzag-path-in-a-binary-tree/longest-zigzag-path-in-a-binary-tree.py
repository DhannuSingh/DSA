# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_len = 0

        # go_left: boolean indicating if the direction to this node was moving left
        # steps: current length of the ZigZag path
        def dfs(node, go_left, steps):
            if not node:
                return
            
            self.max_len = max(self.max_len, steps)

            if go_left:
                # Arrived via left child: 
                # - Moving right continues ZigZag (steps + 1)
                # - Moving left resets path length to 1
                dfs(node.right, False, steps + 1)
                dfs(node.left, True, 1)
            else:
                # Arrived via right child:
                # - Moving left continues ZigZag (steps + 1)
                # - Moving right resets path length to 1
                dfs(node.left, True, steps + 1)
                dfs(node.right, False, 1)

        # Start DFS from root in both possible directions
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return self.max_len