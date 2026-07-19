class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the first occurrence of the character
        idx = word.find(ch)
        
        # If the character doesn't exist, return the original word
        if idx == -1:
            return word
            
        # Reverse the prefix up to idx (inclusive) and join with the rest
        return word[:idx + 1][::-1] + word[idx + 1:]