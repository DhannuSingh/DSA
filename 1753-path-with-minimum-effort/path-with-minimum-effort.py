class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        R, C = len(heights), len(heights[0])
        
        # Matrix to track minimum effort to reach each cell
        efforts = [[float('inf')] * C for _ in range(R)]
        efforts[0][0] = 0
        
        # Min-heap storing (effort, row, col)
        min_heap = [(0, 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            
            # Reached the bottom-right cell
            if r == R - 1 and c == C - 1:
                return effort
            
            # Skip if we already found a better path to this cell
            if effort > efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < R and 0 <= nc < C:
                    # Effort for moving to the neighbor cell
                    next_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))
                        
        return 0