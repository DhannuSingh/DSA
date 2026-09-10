class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        total_sum = sum(batteries)

        # If a battery has more power than total_sum / n, it can continuously
        # power 1 computer for the maximum time and can be excluded.
        while batteries[-1] > total_sum // n:
            total_sum -= batteries.pop()
            n -= 1

        return total_sum // n