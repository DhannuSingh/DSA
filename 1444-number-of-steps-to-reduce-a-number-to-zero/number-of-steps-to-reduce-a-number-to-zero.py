class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2 # num = num // 2
            else:
                num -= 1 # num = num - 1
            steps += 1 # steps = steps + 1
        return steps