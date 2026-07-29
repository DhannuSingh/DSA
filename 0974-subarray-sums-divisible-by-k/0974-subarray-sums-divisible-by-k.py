class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        remainder_map = {0: 1}

        for num in nums:
            current_sum += num
            remainder = current_sum % k

            if remainder in remainder_map:
                count += remainder_map[remainder]
            remainder_map[remainder] = remainder_map.get(remainder, 0) + 1

        return count