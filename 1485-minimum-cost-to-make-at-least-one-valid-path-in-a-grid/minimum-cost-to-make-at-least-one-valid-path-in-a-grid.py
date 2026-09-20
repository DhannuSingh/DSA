class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions corresponding to sign values 1, 2, 3, 4
        # 1: Right, 2: Left, 3: Down, 4: Up
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        
        # Distance array initialized to infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS storing (row, col)
        queue = deque([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            
            # Reached destination
            if r == m - 1 and c == n - 1:
                return dist[r][c]
                
            # Try moving in all 4 directions
            for sign, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    # Cost is 0 if moving in the arrow's direction, else 1
                    cost = 0 if grid[r][c] == sign else 1
                    
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        
                        if cost == 0:
                            queue.appendleft((nr, nc))  # Priority: 0-cost moves
                        else:
                            queue.append((nr, nc))      # Lower priority: 1-cost moves
                            
        return dist[m - 1][n - 1]