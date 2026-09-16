class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Build adjacency list storing (neighbor, direction_flag)
        # direction_flag = 1 if original edge is u -> v (needs reverse if going u -> v)
        # direction_flag = 0 if original edge is v -> u (already pointing towards 0)
        graph = {i: [] for i in range(n)}
        
        for u, v in connections:
            graph[u].append((v, 1))  # Original edge: u -> v
            graph[v].append((u, 0))  # Reverse edge: v -> u

        reorder_count = 0
        visited = {0}
        queue = [0]

        # BFS starting from root node 0
        while queue:
            curr = queue.pop(0)
            
            for neighbor, is_original in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # If it's an original edge pointing away from root, increment count
                    reorder_count += is_original
                    queue.append(neighbor)

        return reorder_count