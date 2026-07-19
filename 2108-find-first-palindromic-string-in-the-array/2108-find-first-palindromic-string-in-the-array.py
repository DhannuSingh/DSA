class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            is_palindrome = True
            
            while left < right:
                if word[left] != word[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1
                
            if is_palindrome:
                return word
                
        return ""