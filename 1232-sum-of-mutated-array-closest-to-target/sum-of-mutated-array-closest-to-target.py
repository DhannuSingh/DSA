class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr.sort()
        n = len(arr)

        prefix_sum = 0
        for i, val in enumerate(arr):
            remaining = n - i
            # If replacing remaining elements with val achieves or exceeds target
            if prefix_sum + val * remaining >= target:
                # Target remainder after subtracting prefix_sum
                rem_target = target - prefix_sum
                ans = rem_target // remaining
                
                # Check whether ans or ans + 1 gives the absolute difference closer to target
                # Priority is given to the smaller value in case of a tie
                diff1 = abs((prefix_sum + ans * remaining) - target)
                diff2 = abs((prefix_sum + (ans + 1) * remaining) - target)

                return ans + 1 if diff2 < diff1 else ans

            prefix_sum += val

        # If even taking max possible values doesn't exceed target, return max element
        return arr[-1]