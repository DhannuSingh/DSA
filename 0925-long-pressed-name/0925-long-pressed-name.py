class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, m = len(name), len(typed)
        
        while j < m:
            # Case 1: Characters match perfectly
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            # Case 2: Mismatch, but it's a long press of the previous character
            elif j > 0 and name[i - 1] == typed[j]:
                j += 1
            # Case 3: Complete mismatch
            else:
                return False
                
        # Return True only if all characters in name were matched
        return i == n