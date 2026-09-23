class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles)

        def backtrack() -> int:
            total_sequences = 0
            
            for char in counts:
                if counts[char] > 0:
                    # Pick this character
                    total_sequences += 1
                    counts[char] -= 1
                    
                    # Recursively build sequences using remaining characters
                    total_sequences += backtrack()
                    
                    # Backtrack
                    counts[char] += 1
                    
            return total_sequences

        return backtrack()