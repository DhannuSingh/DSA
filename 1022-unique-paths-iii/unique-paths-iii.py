class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty_count = 1  # Include starting square
        start_r = start_c = 0

        # Step 1: Find start position and count empty squares
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 0:
                    empty_count += 1

        self.paths = 0

        # Step 2: Backtracking DFS
        def backtrack(r: int, c: int, count: int):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == -1:
                return

            if grid[r][c] == 2:
                if count == 0:
                    self.paths += 1
                return

            # Mark visited
            temp = grid[r][c]
            grid[r][c] = -1

            # Explore 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                backtrack(r + dr, c + dc, count - 1)

            # Unmark (Backtrack)
            grid[r][c] = temp

        backtrack(start_r, start_c, empty_count)
        return self.paths