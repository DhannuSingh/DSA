class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        # Distance to Previous Less Element (PLE)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Distance to Next Less Element (NLE)
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Prefix sums of prefix sums
        # pref[i] = sum(strength[0...i-1])
        # pref_pref[i] = sum(pref[0...i-1])
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] + strength[i]) % MOD

        pref_pref = [0] * (n + 2)
        for i in range(n + 1):
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % MOD

        total = 0
        for i in range(n):
            L = left[i] + 1
            R = right[i] - 1

            # Sum of elements in subsegment sums using prefix sum of prefix sums
            # Right part sum: (i - L + 1) * (pref_pref[R + 2] - pref_pref[i + 1])
            # Left part sum:  (R - i + 1) * (pref_pref[i + 1] - pref_pref[L])
            right_count = R - i + 1
            left_count = i - L + 1

            right_sum = (pref_pref[R + 2] - pref_pref[i + 1]) % MOD
            left_sum = (pref_pref[i + 1] - pref_pref[L]) % MOD

            total_subarray_sum = (left_count * right_sum - right_count * left_sum) % MOD
            total = (total + strength[i] * total_subarray_sum) % MOD

        return total