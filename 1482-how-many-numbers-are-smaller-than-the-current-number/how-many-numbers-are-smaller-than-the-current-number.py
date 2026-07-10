class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Populate frequency bucket array
        counts = [0] * 102
        for num in nums:
            counts[num] += 1

        # Step 2: Transform counts to represent running smaller sums
        running_sum = 0
        for i in range(len(counts)):
            temp = counts[i]
            counts[i] = running_sum
            running_sum += temp
        
        # Step 3: Map original elements to their smaller sums
        return [counts[num] for num in nums]