class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = [""]
        
        for char in s:
            if char.isalpha():
                # For letters, append both lowercase and uppercase variations to existing paths
                res = [sub + c for sub in res for c in (char.lower(), char.upper())]
            else:
                # For digits, simply append the digit to all existing paths
                res = [sub + char for sub in res]
                
        return res