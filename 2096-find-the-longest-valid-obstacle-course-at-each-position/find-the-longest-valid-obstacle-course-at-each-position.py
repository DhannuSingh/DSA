class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        tails = []
        ans = []

        for obstacle in obstacles:
            # Find the first index in tails that is strictly greater than obstacle
            idx = bisect.bisect_right(tails, obstacle)

            if idx == len(tails):
                tails.append(obstacle)
            else:
                tails[idx] = obstacle

            # The length of the longest valid obstacle course ending at this position
            ans.append(idx + 1)

        return ans