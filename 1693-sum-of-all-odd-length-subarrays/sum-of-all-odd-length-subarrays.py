class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            # Number of ways to choose the starting and ending boundaries
            left_choices = i + 1
            right_choices = n - i
            total_subarrays = left_choices * right_choices
            
            # Number of odd-length subarrays containing arr[i]
            odd_subarrays = (total_subarrays + 1) // 2
            
            total_sum += odd_subarrays * arr[i]
            
        return total_sum