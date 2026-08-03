class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def get_next(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = get_next(i)

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[get_next(fast)] > 0:
                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
                slow = get_next(slow)
                fast = get_next(get_next(fast))

            slow = i
            val = nums[i]
            while nums[slow] * val > 0:
                nxt = get_next(slow)
                nums[slow] = 0
                slow = nxt

        return False