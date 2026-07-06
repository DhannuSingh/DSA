class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Repeatedly divide by 2, 4, and 5 as long as divisible
        for factor in[2, 3, 5]:
            while n % factor == 0:
                n //= factor

        # If n was reduced to 1, it only contained 2, 3, or 5
        return n == 1