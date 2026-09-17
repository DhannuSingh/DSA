class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete_count = 0

        # DFS to collect all nodes in the current component
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        # Step 2: Traverse each component and check completeness
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, component)
                
                k = len(component)  # Number of nodes in this component
                is_complete = True
                
                # Each node in a complete component of size k must have degree k - 1
                for node in component:
                    if len(graph[node]) != k - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_count += 1

        return complete_count