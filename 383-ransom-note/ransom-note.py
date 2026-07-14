class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Optimization: A note cannot be longer than the available supply
        if len(ransomNote) > len(magazine):
            return False

        # Count magazine characters
        counts = [0] * 26
        for char in magazine:
            counts[ord(char) - ord('a')] += 1

        # Consume characters for the ransom note
        for char in ransomNote:
            index = ord(char) - ord('a')
            counts[index] -= 1
            if counts[index] < 0:
                return False
        
        return True