class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Attach root_j to root_i and accumulate component size
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

    def get_size(self, i):
        return self.size[self.find(i)]

class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        R, C = len(grid), len(grid[0])
        
        # Mark hit bricks: 2 indicates a brick was originally present and hit
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 2

        dsu = DSU(R * C + 1)
        TOP = R * C  # Virtual top node representing row 0 connectivity

        def get_index(r, c):
            return r * C + c

        # Step 1: Union remaining stable bricks in grid
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    idx = get_index(r, c)
                    if r == 0:
                        dsu.union(idx, TOP)
                    if r > 0 and grid[r - 1][c] == 1:
                        dsu.union(idx, get_index(r - 1, c))
                    if c > 0 and grid[r][c - 1] == 1:
                        dsu.union(idx, get_index(r, c - 1))

        res = [0] * len(hits)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 2: Reverse through hits and restore bricks
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                continue

            grid[r][c] = 1  # Restore brick
            curr_idx = get_index(r, c)
            was_connected = dsu.find(TOP) == dsu.find(curr_idx)
            prev_top_size = dsu.get_size(TOP)

            # Connect with top row if restored at row 0
            if r == 0:
                dsu.union(curr_idx, TOP)

            # Connect with adjacent existing bricks
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    dsu.union(curr_idx, get_index(nr, nc))

            # Count newly stabilized bricks
            if dsu.find(TOP) == dsu.find(curr_idx):
                new_top_size = dsu.get_size(TOP)
                # Count fallen bricks excluding the restored brick itself
                if not was_connected:
                    res[i] = max(0, new_top_size - prev_top_size - 1)

        return res