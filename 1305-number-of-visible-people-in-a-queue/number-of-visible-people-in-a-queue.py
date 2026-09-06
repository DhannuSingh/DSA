class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # Monotonic stack storing heights in decreasing order

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                ans[i] += 1

            # If stack is not empty, the person can see one more person who is taller
            if stack:
                ans[i] += 1

            stack.append(heights[i])

        return ans