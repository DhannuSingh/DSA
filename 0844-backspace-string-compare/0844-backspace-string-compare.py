class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0
        
        while i >= 0 or j >= 0:
            # Find the next valid character in string s
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break
                    
            # Find the next valid character in string t
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            
            # If one string finishes but the other has a valid character left
            if (i >= 0) != (j >= 0):
                return False
                
            # If both have valid characters, compare them
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
                
            i -= 1
            j -= 1
        return True