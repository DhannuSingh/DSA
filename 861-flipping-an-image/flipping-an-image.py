class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == row[right]:
                    # XOR with 1 flips a binary bit (0->1, 1->0)
                    row[left] = row[right] = row[left] ^ 1
                left += 1
                right -= 1
        return image