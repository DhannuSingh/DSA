class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        for i in range(31, -1, -1):
            if (a >> i) >= b:
                quotient += 1 << i
                a -= b << i

        return -quotient if negative else quotient