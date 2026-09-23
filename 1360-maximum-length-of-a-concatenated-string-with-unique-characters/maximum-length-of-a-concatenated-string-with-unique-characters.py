class Solution:
    def maxLength(self, arr: list[str]) -> int:
        masks = [0]  # Base case: empty string mask

        for s in arr:
            # Check if string s contains unique characters internally
            if len(set(s)) != len(s):
                continue
            
            # Convert string s to a bitmask
            mask = 0
            for char in s:
                mask |= 1 << (ord(char) - ord('a'))

            # Combine with previously generated unique masks
            new_masks = []
            for existing in masks:
                if not (existing & mask):
                    new_masks.append(existing | mask)
            
            masks.extend(new_masks)

        # Return max count of set bits among all generated valid combinations
        return max(mask.bit_count() for mask in masks)