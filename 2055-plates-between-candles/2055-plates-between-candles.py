class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        candles = [i for i, ch in enumerate(s) if ch == '|']
        
        nearest_right = [-1] * n
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i
            nearest_right[i] = last
            
        nearest_left = [-1] * n
        last = -1
        for i in range(n):
            if s[i] == '|':
                last = i
            nearest_left[i] = last
            
        ans = []
        for left, right in queries:
            c1 = nearest_right[left]
            c2 = nearest_left[right]
            
            if c1 != -1 and c2 != -1 and c1 < c2:
                total_between = c2 - c1
                c1_idx = bisect.bisect_left(candles, c1)
                c2_idx = bisect.bisect_left(candles, c2)
                num_candles = c2_idx - c1_idx + 1
                ans.append(total_between - num_candles + 1)
            else:
                ans.append(0)
                
        return ans