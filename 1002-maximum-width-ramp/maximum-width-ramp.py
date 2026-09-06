class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []
        n = len(nums)

        # Build a strictly decreasing stack of candidate left indices
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0

        # Traverse from right to left to find the maximum width ramp
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())

        return max_width