class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        deque = []  # Monotonic deque storing indices of max DP values
        
        for i in range(n):
            # Remove indices out of the k-distance window
            if deque and deque[0] < i - k:
                deque.pop(0)
            
            # Max possible DP value from previous window
            max_prev = dp[deque[0]] if deque else 0
            dp[i] = nums[i] + max(0, max_prev)
            
            # Maintain decreasing order in deque
            while deque and dp[deque[-1]] <= dp[i]:
                deque.pop()
            
            deque.append(i)
        
        return max(dp)