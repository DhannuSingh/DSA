class Solution:

  def reverse(self, x: int) -> int:
    # Define 32-bit signed integer limits
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -(2**31)  # -2147483648

    rev = 0
    # Use sign multiplier to simplify logic for negative numbers
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
      pop = x % 10
      x //= 10

      # Check for overflow before multiplying rev by 10
      if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
        return 0

      rev = rev * 10 + pop

    return rev * sign