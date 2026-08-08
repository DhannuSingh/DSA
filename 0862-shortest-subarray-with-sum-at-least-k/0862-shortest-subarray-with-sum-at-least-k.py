class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
            
        res = float('inf')
        q = collections.deque()
        
        for i, curr_sum in enumerate(prefix_sums):
            while q and curr_sum - prefix_sums[q[0]] >= k:
                res = min(res, i - q.popleft())
                
            while q and curr_sum <= prefix_sums[q[-1]]:
                q.pop()
                
            q.append(i)
            
        return res if res != float('inf') else -1
