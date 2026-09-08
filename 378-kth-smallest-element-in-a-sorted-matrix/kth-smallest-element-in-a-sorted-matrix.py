class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        # Min-heap storing tuples of (value, row, col)
        # Initialize with the first element of each row up to min(n, k)
        heap = [(matrix[r][0], r, 0) for r in range(min(n, k))]
        heapq.heapify(heap)

        val = 0
        for _ in range(k):
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return val