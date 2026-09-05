class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        MOD = 10**9 + 7

        # Precompute powers of 2 modulo 10^9 + 7
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        left = 0
        right = n - 1
        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return count