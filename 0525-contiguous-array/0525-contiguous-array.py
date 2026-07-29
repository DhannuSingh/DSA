class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count_map = {0: -1}
        max_len = 0
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1

            if current_sum in count_map:
                max_len = max(max_len, i - count_map[current_sum])
            else:
                count_map[current_sum] = i

        return max_len