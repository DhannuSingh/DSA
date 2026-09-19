class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        n = len(passingFees)
        
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        # Min-heap storing (total_cost, total_time, current_node)
        min_heap = [(passingFees[0], 0, 0)]
        
        # Track the minimum time to reach each node
        min_time = [float('inf')] * n
        min_time[0] = 0
        
        while min_heap:
            cost, time, node = heapq.heappop(min_heap)
            
            # Reached destination within maxTime
            if node == n - 1:
                return cost
            
            # Explore neighbors
            for neighbor, travel_time in graph[node]:
                next_time = time + travel_time
                next_cost = cost + passingFees[neighbor]
                
                # Only proceed if within maxTime limit and improves time to reach neighbor
                if next_time <= maxTime and next_time < min_time[neighbor]:
                    min_time[neighbor] = next_time
                    heapq.heappush(min_heap, (next_cost, next_time, neighbor))
                    
        return -1