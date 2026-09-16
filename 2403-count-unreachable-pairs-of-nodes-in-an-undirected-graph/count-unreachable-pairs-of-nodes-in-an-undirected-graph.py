class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build the adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        component_sizes = []
        
        # Step 2: DFS to find the size of each connected component
        def dfs(node):
            visited[node] = True
            size = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    size += dfs(neighbor)
            return size

        for i in range(n):
            if not visited[i]:
                component_sizes.append(dfs(i))
        
        # Step 3: Compute unreachable pairs
        total_unreachable = 0
        remaining_nodes = n
        
        for size in component_sizes:
            # Current component nodes can pair up with all remaining nodes outside this component
            total_unreachable += size * (remaining_nodes - size)
            remaining_nodes -= size
            
        return total_unreachable