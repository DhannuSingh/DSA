class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        # Count total frequencies of 'a', 'b', and 'c'
        total = {'a': 0, 'b': 0, 'c': 0}
        for char in s:
            total[char] += 1

        # If any character appears fewer than k times, it's impossible
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1

        # Maximum allowed counts inside the window to leave at least k outside
        max_in_window = {
            'a': total['a'] - k,
            'b': total['b'] - k,
            'c': total['c'] - k
        }

        # Find the maximum length of a subarray that stays within allowed counts
        window = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        max_len = 0

        for right in range(len(s)):
            window[s[right]] += 1

            while (window['a'] > max_in_window['a'] or
                   window['b'] > max_in_window['b'] or
                   window['c'] > max_in_window['c']):
                window[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return len(s) - max_len