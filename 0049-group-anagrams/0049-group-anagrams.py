from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)

    for s in strs:
      count = [0] * 26
      for char in s:
        count[ord(char) - ord("a")] += 1

      # Tuple of counts is immutable and usable as a hash map key
      ans[tuple(count)].append(s)

    return list(ans.values())