class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired_chars = set()
        length = 0

        for char in s:
            if char in unpaired_chars:
                # We found a matching pair! Add 2 to the length
                unpaired_chars.remove(char)
                length += 2
            else:
                unpaired_chars.add(char)
        # If any unmatched character is left over, it can go in the center
        return length + 1 if unpaired_chars else length