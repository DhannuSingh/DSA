class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Track 1st and 2nd minimum distances (in number of edges)
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        
        dist1[1] = 0
        queue = deque([(1, 0)])  # (node, edge_count)

        # BFS to find the second shortest path in terms of edge count
        while queue:
            node, d = queue.popleft()

            for neighbor in graph[node]:
                # Found a new strictly shorter path
                if dist1[neighbor] == -1:
                    dist1[neighbor] = d + 1
                    queue.append((neighbor, d + 1))
                # Found a strictly second shorter path
                elif dist2[neighbor] == -1 and dist1[neighbor] < d + 1:
                    dist2[neighbor] = d + 1
                    queue.append((neighbor, d + 1))

        # Second minimum edge count to reach node n
        second_min_edges = dist2[n]

        # Step 3: Convert edge count to actual elapsed time considering red lights
        curr_time = 0
        for _ in range(second_min_edges):
            # If current time falls on a RED light interval
            if (curr_time // change) % 2 == 1:
                # Wait for green light
                curr_time += change - (curr_time % change)
            curr_time += time

        return curr_time