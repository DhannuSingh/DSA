class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        ans = []

        def dfs(node: int, path: list[int]):
            if node == target:
                ans.append(list(path))
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # Backtrack

        dfs(0, [0])
        return ans