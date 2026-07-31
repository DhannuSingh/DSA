import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            total_sum = sum(math.ceil(num / mid) for num in nums)
            
            if total_sum <= threshold:
                right = mid
            else:
                left = mid + 1
                
        return left