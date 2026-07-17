class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                        live_neighbors += 1

                if board[r][c] ==  1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3

        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1