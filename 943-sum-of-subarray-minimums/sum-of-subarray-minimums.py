class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # Distance to Next Smaller Element (NSE)
        # Distance to Previous Smaller or Equal Element (PLE)
        ple = [0] * n
        nse = [0] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ple[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            nse[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + arr[i] * ple[i] * nse[i]) % MOD

        return total_sum