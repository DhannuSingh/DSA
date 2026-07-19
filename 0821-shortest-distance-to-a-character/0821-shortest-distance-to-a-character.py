class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [0] * n
        
        # Pass 1: Left to Right
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev
            
        # Pass 2: Right to Left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)
            
        return res