class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        current_sum = sum(arr[:k])
        ans = 1 if current_sum >= target_sum else 0
        
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                ans += 1
                
        return ans