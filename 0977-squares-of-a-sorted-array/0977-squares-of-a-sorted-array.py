class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        
        # Fill the result array from right to left
        for p in range(n - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                res[p] = left_square
                left += 1
            else:
                res[p] = right_square
                right -= 1
        return res
        return res