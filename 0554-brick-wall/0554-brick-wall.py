from collections import defaultdict


class Solution:

  def leastBricks(self, wall: list[list[int]]) -> int:
    edge_counts = defaultdict(int)

    for row in wall:
      edge_pos = 0
      # Skip the last brick in each row to avoid measuring the outer wall boundaries
      for brick in row[:-1]:
        edge_pos += brick
        edge_counts[edge_pos] += 1

    max_edges = max(edge_counts.values()) if edge_counts else 0
    return len(wall) - max_edges