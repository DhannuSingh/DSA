class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        res = 0
        stack = [float('inf')]

        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                res += mid * min(stack[-1], num)
            stack.append(num)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res