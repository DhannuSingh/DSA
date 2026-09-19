class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        # Step 2: Initialize dist and ways arrays
        dist = [float('inf')] * n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap storing (distance, node)
        min_heap = [(0, 0)]
        
        while min_heap:
            d, u = heapq.heappop(min_heap)
            
            # Skip outdated entries in the heap
            if d > dist[u]:
                continue
                
            for v, w in graph[u]:
                # Found a strictly shorter path to node v
                if d + w < dist[v]:
                    dist[v] = d + w
                    ways[v] = ways[u]
                    heapq.heappush(min_heap, (dist[v], v))
                    
                # Found another path to node v with the same minimum length
                elif d + w == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
                    
        return ways[n - 1]