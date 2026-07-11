class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1

        # Iterate backwards from the last index to 0
        for i in range(len(arr) -1, -1, -1):
            original_val = arr[i]
            arr[i] = max_seen
            max_seen = max(max_seen, original_val)

        return arr