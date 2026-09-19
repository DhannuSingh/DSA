class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        # Step 2: Dijkstra's Algorithm from destination node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        min_heap = [(0, n)]  # (distance, node)
        
        while min_heap:
            d, node = heapq.heappop(min_heap)
            
            if d > dist[node]:
                continue
                
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
                    
        # Step 3: DFS + Memoization to count restricted paths
        memo = {}
        
        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]
            
            total_paths = 0
            for neighbor, _ in graph[node]:
                # Restricted path condition: distToLastNode(node) > distToLastNode(neighbor)
                if dist[node] > dist[neighbor]:
                    total_paths = (total_paths + dfs(neighbor)) % MOD
                    
            memo[node] = total_paths
            return memo[node]
            
        return dfs(1)