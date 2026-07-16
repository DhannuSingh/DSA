class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000 for num in nums)