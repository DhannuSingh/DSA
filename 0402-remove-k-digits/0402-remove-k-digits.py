class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
            
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        if k > 0:
            stack = stack[:-k]
            
        res = "".join(stack).lstrip("0")
        return res if res else "0"
