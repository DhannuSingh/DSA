class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        letter_counts = Counter(letters)
        
        def can_form(word: str) -> bool:
            word_counts = Counter(word)
            return all(letter_counts[char] >= count for char, count in word_counts.items())

        def get_word_score(word: str) -> int:
            return sum(score[ord(char) - ord('a')] for char in word)

        def backtrack(index: int) -> int:
            if index == len(words):
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1)
            
            # Option 2: Include the current word (if enough letters are available)
            word = words[index]
            if can_form(word):
                # Deduct letters used by the word
                for char in word:
                    letter_counts[char] -= 1
                
                # Recurse with added word score
                current_score = get_word_score(word) + backtrack(index + 1)
                max_score = max(max_score, current_score)
                
                # Backtrack (restore letter counts)
                for char in word:
                    letter_counts[char] += 1

            return max_score

        return backtrack(0)