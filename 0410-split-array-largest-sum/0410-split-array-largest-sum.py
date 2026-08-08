class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = num
                    if count > k:
                        return False
                else:
                    curr_sum += num
            return True

        low = max(nums)
        high = sum(nums)
        res = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_split(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
