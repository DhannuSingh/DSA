class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                prev_idx = stack.pop()
                res[prev_idx] = nums[idx]
            if i < n:
                stack.append(idx)
                
        return res
