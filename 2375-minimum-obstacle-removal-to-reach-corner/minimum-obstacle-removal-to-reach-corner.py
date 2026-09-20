class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Distance array initialized to infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS: stores (row, col)
        queue = deque([(0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            # Reached the destination corner
            if r == m - 1 and c == n - 1:
                return dist[r][c]
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    
                    # If a shorter path to (nr, nc) is found
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        
                        if weight == 0:
                            queue.appendleft((nr, nc))  # Cost 0 -> higher priority
                        else:
                            queue.append((nr, nc))      # Cost 1 -> lower priority
                            
        return dist[m - 1][n - 1]