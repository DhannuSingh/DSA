class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        insert_index = 1
        for i in range(1, len(nums)):
            # If current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index