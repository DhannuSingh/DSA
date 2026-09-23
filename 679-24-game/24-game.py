class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        EPSILON = 1e-6

        def backtrack(nums: list[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    # Extract remaining numbers
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    
                    a, b = nums[i], nums[j]
                    
                    # Generate all valid outcomes for two numbers
                    possible_results = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPSILON:
                        possible_results.append(a / b)
                    if abs(a) > EPSILON:
                        possible_results.append(b / a)

                    # Try each outcome recursively
                    for res in possible_results:
                        if backtrack(next_nums + [res]):
                            return True

            return False

        return backtrack([float(c) for c in cards])