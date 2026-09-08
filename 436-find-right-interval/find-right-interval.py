class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        # Store sorted starting points along with their original indices
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_vals = [s[0] for s in starts]
        
        result = []
        for interval in intervals:
            end = interval[1]
            # Find the smallest start value >= current interval's end
            idx = bisect.bisect_left(start_vals, end)
            
            if idx < len(starts):
                result.append(starts[idx][1])
            else:
                result.append(-1)

        return result