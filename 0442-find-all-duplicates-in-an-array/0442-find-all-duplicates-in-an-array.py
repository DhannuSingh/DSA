class Solution:

  def findDuplicates(self, nums: list[int]) -> list[int]:
    res = []

    for num in nums:
      val = abs(num)
      idx = val - 1

      # If already negative, we've encountered this number before
      if nums[idx] < 0:
        res.append(val)
      else:
        # Mark as visited by negating
        nums[idx] = -nums[idx]

    return res