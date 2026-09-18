class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        
        # Step 1: Build graph adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Group node indices by their values
        val_to_nodes = defaultdict(list)
        for i, val in enumerate(vals):
            val_to_nodes[val].append(i)

        dsu = DSU(n)
        good_paths = n  # Every individual node is a valid path of length 0

        # Step 3: Process values in ascending order
        for val in sorted(val_to_nodes.keys()):
            nodes = val_to_nodes[val]

            # Union current nodes with neighbors that have value <= current val
            for u in nodes:
                for v in graph[u]:
                    if vals[v] <= val:
                        dsu.union(u, v)

            # Count frequency of current val in each connected component
            component_counts = defaultdict(int)
            for u in nodes:
                root = dsu.find(u)
                component_counts[root] += 1

            # For each component with c nodes of value 'val', add c * (c - 1) // 2 paths
            for root, count in component_counts.items():
                good_paths += count * (count - 1) // 2

        return good_paths