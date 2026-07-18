class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # An empty string is always a subsequence of any string
        if not s:
            return True
            
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
                # If we've matched all characters in s, we're done
                if i == len(s):
                    return True
                    
        return False