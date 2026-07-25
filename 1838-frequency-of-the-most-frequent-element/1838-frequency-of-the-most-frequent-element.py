class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        ans = 0
        
        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans