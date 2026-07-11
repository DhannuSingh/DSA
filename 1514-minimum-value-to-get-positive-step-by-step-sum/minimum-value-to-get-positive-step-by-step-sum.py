class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = 0
        min_running_sum = 0

        for num in nums:
            running_sum += num
            min_running_sum = min(min_running_sum, running_sum)

        # If min_running_sum is negative, we need 1 - min_running_sum
        # Otherwise, the minimum allowed positive startValue is 1
        return max(1, 1 - min_running_sum)