class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Build frequency map
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Find the first character with a count of 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        return -1