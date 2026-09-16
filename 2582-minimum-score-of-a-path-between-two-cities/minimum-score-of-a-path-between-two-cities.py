class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Build adjacency list storing (neighbor, distance)
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        # Step 2: Traverse the connected component containing city 1
        visited = set()
        queue = [1]
        visited.add(1)
        
        min_score = float('inf')
        
        while queue:
            node = queue.pop(0)
            
            for neighbor, weight in graph[node]:
                # Consider weight of all edges in the connected component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score