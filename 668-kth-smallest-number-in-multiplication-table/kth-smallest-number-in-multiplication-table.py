class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x: int) -> int:
            count = 0
            for r in range(1, m + 1):
                count += min(x // r, n)
            return count

        left, right = 1, m * n
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_less_equal(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans