class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab = (a * b) // math.gcd(a, b)
        lcm_bc = (b * c) // math.gcd(b, c)
        lcm_ac = (a * c) // math.gcd(a, c)
        lcm_abc = (lcm_ab * c) // math.gcd(lcm_ab, c)
        
        def count_divisible(mid):
            return (mid // a + mid // b + mid // c 
                    - mid // lcm_ab - mid // lcm_bc - mid // lcm_ac 
                    + mid // lcm_abc)
        
        low = 1
        high = 2 * (10 ** 9)
        res = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_divisible(mid) >= n:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
