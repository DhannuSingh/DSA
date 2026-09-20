class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        # Step 1: Build the adjacency list
        # Each edge has weight = cnt + 1
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))

        # Step 2: Dijkstra's Algorithm to find shortest path to all original nodes
        dist = {i: float('inf') for i in range(n)}
        dist[0] = 0
        min_heap = [(0, 0)]  # (distance, node)

        while min_heap:
            d, u = heapq.heappop(min_heap)

            if d > dist[u]:
                continue

            for v, weight in graph[u]:
                if d + weight < dist[v]:
                    dist[v] = d + weight
                    heapq.heappush(min_heap, (dist[v], v))

        # Step 3: Count reachable original nodes
        ans = sum(1 for i in range(n) if dist[i] <= maxMoves)

        # Step 4: Count reachable sub-nodes along each edge
        for u, v, cnt in edges:
            # Sub-nodes reached from u
            reach_u = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            # Sub-nodes reached from v
            reach_v = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0

            # Sub-nodes covered cannot exceed total sub-nodes on this edge
            ans += min(cnt, reach_u + reach_v)

        return ans