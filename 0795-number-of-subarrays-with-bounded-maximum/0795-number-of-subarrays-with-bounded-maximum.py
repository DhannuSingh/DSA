class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        l = -1
        r = -1
        
        for i, num in enumerate(nums):
            if num > right:
                l = i
            if num >= left:
                r = i
            ans += r - l
            
        return ans