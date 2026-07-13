class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Fixed array for 26 lowercase English characters
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # If any element is non-zero, s and t are not anagrams
        return all(x == 0 for x in count)