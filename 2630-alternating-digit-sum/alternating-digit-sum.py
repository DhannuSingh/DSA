class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total_sum = 0
        sign = 1

        for digit in str(n):
            total_sum += sign * int(digit)
            sign = -sign
        return total_sum