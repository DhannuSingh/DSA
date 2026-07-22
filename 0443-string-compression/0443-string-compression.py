class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_len = 1
            while i + group_len < len(chars) and chars[i + group_len] == chars[i]:
                group_len += 1
            chars[res] = chars[i]
            res += 1
            if group_len > 1:
                for c in str(group_len):
                    chars[res] = c
                    res += 1
            i += group_len
        return res