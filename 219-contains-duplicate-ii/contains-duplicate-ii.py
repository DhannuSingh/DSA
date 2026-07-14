class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            # If the window grows larger than k, slide the left boundary forward
            if i > k:
                window.remove(nums[i - k - 1])
            # If the element is already in our set, a duplicate exists within distance k
            if num in window:
                return True

            window.add(num)

        return False