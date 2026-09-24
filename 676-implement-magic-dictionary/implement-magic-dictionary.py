class MagicDictionary:

    def __init__(self):
        # Map word length to list of words of that length
        self.words_by_len = defaultdict(list)

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self.words_by_len[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        
        # Only check words with the same length as searchWord
        for word in self.words_by_len[n]:
            diff_count = 0
            for char1, char2 in zip(searchWord, word):
                if char1 != char2:
                    diff_count += 1
                    if diff_count > 1:
                        break  # Early exit if more than 1 character differs
            
            # Exactly one character must be different
            if diff_count == 1:
                return True
                
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)