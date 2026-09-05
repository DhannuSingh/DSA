class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        dq = deque()  # Stores pairs of (y - x, x)
        max_val = float('-inf')

        for x, y in points:
            # Remove points outside the range x_j - x_i > k
            while dq and x - dq[0][1] > k:
                dq.popleft()

            # The current maximum value for point (x, y) is y + x + max(y_i - x_i)
            if dq:
                max_val = max(max_val, x + y + dq[0][0])

            # Maintain monotonic deque for (y_j - x_j) in decreasing order
            diff = y - x
            while dq and dq[-1][0] <= diff:
                dq.pop()

            dq.append((diff, x))

        return max_val