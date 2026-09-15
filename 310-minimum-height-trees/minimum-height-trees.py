class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        # Edge cases: 1 or 2 nodes are already the centroids
        if n <= 2:
            return [i for i in range(n)]
        
        # Step 1: Build adjacency list and degree list
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        # Step 2: Initialize queue with all current leaf nodes
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        
        # Step 3: Trim leaves layer by layer until <= 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                # Get the sole neighbor of the leaf
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add to next layer
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
            
        return leaves