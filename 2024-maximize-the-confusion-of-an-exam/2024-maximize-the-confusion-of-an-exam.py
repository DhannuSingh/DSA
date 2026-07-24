class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = 0
        count = collections.Counter()
        l = 0
        
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1
            max_freq = max(max_freq, count[answerKey[r]])

            if (r - l + 1) - max_freq > k:
                count[answerKey[l]] -= 1
                l += 1
                
        return len(answerKey) - l