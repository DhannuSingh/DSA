class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert string to a list since strings are immutable in Python
        chars = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(chars) - 1
        
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and chars[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and chars[right] not in vowels:
                right -= 1
                
            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]
            
            left += 1
            right -= 1
            
        return "".join(chars)