class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Min-heap storing (time, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        
        visited = set([(0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            
            # Reached destination
            if r == n - 1 and c == n - 1:
                return t
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Water level required for neighbor cell is max(current_time, neighbor_elevation)
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
                    
        return -1