# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list:
        if not root or not target:
            return []
        
        parents = {}

        # Step 1: Map each node to its parent using DFS
        def find_parents(node, parent=None):
            if node:
                parents[node] = parent
                find_parents(node.left, node)
                find_parents(node.right, node)

        find_parents(root)

        # Step 2: BFS starting from target node
        queue = [target]
        visited = {target}
        current_distance = 0

        while queue:
            if current_distance == k:
                return [node.val for node in queue]
            
            next_level = []
            for node in queue:
                # Explore neighbors: left child, right child, and parent
                for neighbor in (node.left, node.right, parents[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)
            
            queue = next_level
            current_distance += 1

        return []