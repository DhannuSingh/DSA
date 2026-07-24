class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0

        n = len(nums)
        curr_ones = sum(nums[:total_ones])
        max_ones = curr_ones

        for i in range(1, n):
            curr_ones += nums[(i + total_ones - 1) % n] - nums[i - 1]
            max_ones = max(max_ones, curr_ones)

        return total_ones - max_ones