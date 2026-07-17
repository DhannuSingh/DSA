class Solution:

    def __init__(self, nums: List[int]):
        self.original = list(nums)
        self.array = nums

    def reset(self) -> List[int]:
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)

            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()