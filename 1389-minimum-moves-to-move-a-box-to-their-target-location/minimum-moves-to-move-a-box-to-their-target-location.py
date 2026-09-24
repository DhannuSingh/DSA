class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # Locate initial positions of Player (S), Box (B), and Target (T)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'S':
                    start_player = (r, c)
                elif grid[r][c] == 'B':
                    start_box = (r, c)
                elif grid[r][c] == 'T':
                    target = (r, c)
        
        # Helper to check if player can reach (tx, ty) from (sx, sy) without crossing walls or the current box position
        def can_reach(start, target_pos, current_box):
            if start == target_pos:
                return True
            
            q = deque([start])
            visited = {start}
            
            while q:
                r, c = q.popleft()
                if (r, c) == target_pos:
                    return True
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and (nr, nc) != current_box:
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            return False

        # Queue for 0-1 BFS: (pushes, box_r, box_c, player_r, player_c)
        # deque allows popping from left and appending to left/right for 0-1 BFS
        q = deque([(0, start_box[0], start_box[1], start_player[0], start_player[1])])
        visited = set([(start_box[0], start_box[1], start_player[0], start_player[1])])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            pushes, bx, by, px, py = q.popleft()

            # Target reached
            if (bx, by) == target:
                return pushes

            # Try pushing the box in 4 directions
            for dx, dy in directions:
                nbx, nby = bx + dx, by + dy  # New box position
                ppx, ppy = bx - dx, by - dy  # Required player position to push the box

                # Check if new box position and player push position are valid grid cells
                if 0 <= nbx < R and 0 <= nby < C and grid[nbx][nby] != '#':
                    if 0 <= ppx < R and 0 <= ppy < C and grid[ppx][ppy] != '#':
                        # Check if state already visited
                        if (nbx, nby, bx, by) not in visited:
                            # Check if player can move to (ppx, ppy)
                            if can_reach((px, py), (ppx, ppy), (bx, by)):
                                visited.add((nbx, nby, bx, by))
                                q.append((pushes + 1, nbx, nby, bx, by))

        return -1