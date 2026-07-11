class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
            
        left, right = 0, n - 1
        
        # Walk up from the left
        while left + 1 < n and arr[left] < arr[left + 1]:
            left += 1
            
        # Walk up from the right
        while right - 1 >= 0 and arr[right] < arr[right - 1]:
            right -= 1
            
        # Check if they met at the same peak, and the peak isn't a boundary
        return left == right and left > 0 and right < n - 1