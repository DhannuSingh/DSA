class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # Step 1: Build the adjacency list for the graph
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        # Color map: 0 = uncolored, 1 = color A, -1 = color B
        colors = {}
        
        # Step 2: BFS coloring for each connected component
        for person in range(1, n + 1):
            if person in colors:
                continue
            
            queue = [person]
            colors[person] = 1  # Start coloring current component with color 1
            
            while queue:
                curr = queue.pop(0)
                
                for neighbor in graph[curr]:
                    # Conflict found: neighbor has the same color as current node
                    if neighbor in colors:
                        if colors[neighbor] == colors[curr]:
                            return False
                    else:
                        # Color neighbor with opposite color
                        colors[neighbor] = -colors[curr]
                        queue.append(neighbor)
                        
        return True