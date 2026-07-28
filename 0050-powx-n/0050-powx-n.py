class Solution:

    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x = 1 / x
            N = -N

        ans = 1.0
        curr_product = x
        while N > 0:
            if N % 2 == 1:
                ans *= curr_product
            curr_product *= curr_product
            N //= 2

        return ans