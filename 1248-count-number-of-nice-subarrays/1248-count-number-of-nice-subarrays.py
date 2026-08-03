class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k: int) -> int:
            left = 0
            count = 0
            ans = 0
            for right in range(len(nums)):
                count += nums[right] % 2
                while count > k:
                    count -= nums[left] % 2
                    left += 1
                ans += right - left + 1
            return ans

        return atMost(k) - atMost(k - 1)