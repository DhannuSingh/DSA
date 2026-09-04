class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        total_profit = 0
        max_profit = 0
        i = 0
        n = len(jobs)

        for w in worker:
            while i < n and jobs[i][0] <= w:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit

        return total_profit