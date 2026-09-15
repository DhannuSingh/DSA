class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # Step 1: Build the adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: BFS traversal starting from source
        queue = [source]
        visited = {source}
        
        while queue:
            node = queue.pop(0)
            
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False