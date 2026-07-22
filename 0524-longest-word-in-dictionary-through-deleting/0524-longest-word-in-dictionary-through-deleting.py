class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ""
        for word in dictionary:
            if len(word) < len(ans) or (len(word) == len(ans) and word > ans):
                continue
            
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            
            if i == len(word):
                ans = word
                
        return ans