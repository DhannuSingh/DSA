class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # First pass: Find the highest number of candies currently held
        max_candies = max(candies)
        
        # Second pass: Evaluate each child and return the boolean list
        return [candy + extraCandies >= max_candies for candy in candies]