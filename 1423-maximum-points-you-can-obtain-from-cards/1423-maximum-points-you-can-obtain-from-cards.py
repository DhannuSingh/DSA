class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total_pts = sum(cardPoints[:k])
        max_pts = total_pts

        for i in range(1, k + 1):
            total_pts += cardPoints[-i] - cardPoints[k - i]
            max_pts = max(max_pts, total_pts)

        return max_pts