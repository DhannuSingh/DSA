class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Step 2: Floyd-Warshall Algorithm to find all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Step 3: Count reachable cities within threshold for each city
        min_reachable_count = float('inf')
        result_city = -1

        for i in range(n):
            reachable_count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            # Prefer smaller reachable count; tie-breaker: larger city index
            if reachable_count <= min_reachable_count:
                min_reachable_count = reachable_count
                result_city = i

        return result_city