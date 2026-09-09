class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Binary search for the starting index of the k-length window
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Compare distance of x to arr[mid] vs arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]