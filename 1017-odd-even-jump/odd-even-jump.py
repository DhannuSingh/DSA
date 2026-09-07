class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        # Find the next higher and next lower jump indices using a stack after sorting
        next_higher = [0] * n
        next_lower = [0] * n

        # Helper to compute next greater/smaller index using a monotonic stack
        def get_next_indices(indices):
            result = [0] * n
            stack = []
            for idx in indices:
                while stack and stack[-1] < idx:
                    result[stack.pop()] = idx
                stack.append(idx)
            return result

        # Sort indices by value ascending; for equal values, index ascending
        sorted_indices = sorted(range(n), key=lambda i: (arr[i], i))
        next_higher = get_next_indices(sorted_indices)

        # Sort indices by value descending; for equal values, index ascending
        sorted_indices.sort(key=lambda i: (-arr[i], i))
        next_lower = get_next_indices(sorted_indices)

        # odd[i]: Can reach the end starting from index i with an odd jump (1st, 3rd, ...)
        # even[i]: Can reach the end starting from index i with an even jump (2nd, 4th, ...)
        odd = [False] * n
        even = [False] * n

        odd[-1] = True
        even[-1] = True

        for i in range(n - 2, -1, -1):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]

        return sum(odd)