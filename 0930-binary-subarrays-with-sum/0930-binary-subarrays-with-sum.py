class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            current_sum = 0
            ans = 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans

        return atMost(goal) - atMost(goal - 1)