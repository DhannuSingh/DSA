class Solution:

  def nthUglyNumber(self, n: int) -> int:
    ugly = [1] * n
    i2 = i3 = i5 = 0

    for i in range(1, n):
      next_2 = ugly[i2] * 2
      next_3 = ugly[i3] * 3
      next_5 = ugly[i5] * 5

      next_ugly = min(next_2, next_3, next_5)
      ugly[i] = next_ugly

      # Advance pointers if they produced the minimum
      if next_ugly == next_2:
        i2 += 1
      if next_ugly == next_3:
        i3 += 1
      if next_ugly == next_5:
        i5 += 1

    return ugly[-1]