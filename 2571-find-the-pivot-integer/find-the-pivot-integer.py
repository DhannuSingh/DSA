class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2

        x = int(math.isqrt(total_sum))

        return x if x * x == total_sum else -1