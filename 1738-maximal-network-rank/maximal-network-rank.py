class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n
        connected = set()
        
        # Count degrees and store connected pairs in a set for O(1) lookup
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            connected.add((u, v))
            connected.add((v, u))
            
        max_rank = 0
        
        # Check all pairs of cities (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                current_rank = degree[i] + degree[j]
                
                # If there's a direct road between i and j, subtract 1
                if (i, j) in connected:
                    current_rank -= 1
                    
                max_rank = max(max_rank, current_rank)
                
        return max_rank