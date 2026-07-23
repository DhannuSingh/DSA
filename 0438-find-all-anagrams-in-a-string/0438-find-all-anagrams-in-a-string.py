from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
            
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        
        res = []
        if p_count == s_count:
            res.append(0)
            
        left = 0
        for right in range(len(p), len(s)):
            s_count[s[right]] += 1
            s_count[s[left]] -= 1
            
            if s_count[s[left]] == 0:
                del s_count[s[left]]
                
            left += 1
            
            if p_count == s_count:
                res.append(left)
                
        return res