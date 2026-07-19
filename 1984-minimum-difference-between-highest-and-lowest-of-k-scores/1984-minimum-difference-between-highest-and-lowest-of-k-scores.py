class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # If we only pick 1 student, the max and min score are the same
        if k == 1:
            return 0
            
        nums.sort()
        min_diff = float('inf')
        
        # Slide a window of size k across the sorted array
        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff