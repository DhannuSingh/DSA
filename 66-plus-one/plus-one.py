class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move backwards
        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If it's a 9, it becomes 0 due to the carry
            digits[i] = 0
        # If we exit the loop, all digits were 9 (e.g., 999 -> 000)
        # We need to prepend a 1
        return [1] + digits