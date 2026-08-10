class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        num_k = float('-inf')
        
        for num in reversed(nums):
            if num < num_k:
                return True
            while stack and stack[-1] < num:
                num_k = stack.pop()
            stack.append(num)
            
        return False
