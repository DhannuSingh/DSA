class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        counts = defaultdict(int)

        for num in nums:
            # Add the number of times we have seen this number before
            ans += counts[num]
            # Increment the count of this number
            counts[num] += 1
        return ans