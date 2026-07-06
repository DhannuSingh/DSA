import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                sum_squares = a * a + b * b
                c = int(math.sqrt(sum_squares))

                if c <= n and c * c == sum_squares:
                    count += 1
        return count