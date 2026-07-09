class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            # Sum up the current customer's accounts and update max
            max_wealth = max(max_wealth, sum(customer))
        return max_wealth