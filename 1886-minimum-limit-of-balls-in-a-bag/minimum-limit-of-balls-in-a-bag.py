class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def canDivide(max_balls: int) -> bool:
            ops = 0
            for num in nums:
                # Number of operations needed to make all bags have at most max_balls
                ops += (num - 1) // max_balls
                if ops > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller maximum bag size
            else:
                left = mid + 1   # Increase allowed maximum bag size

        return ans