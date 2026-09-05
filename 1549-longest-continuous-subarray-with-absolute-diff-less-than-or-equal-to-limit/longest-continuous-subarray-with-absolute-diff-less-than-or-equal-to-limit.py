class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_len = 0

        for right, num in enumerate(nums):
            while min_deque and min_deque[-1] > num:
                min_deque.pop()
            while max_deque and max_deque[-1] < num:
                max_deque.pop()

            min_deque.append(num)
            max_deque.append(num)

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len