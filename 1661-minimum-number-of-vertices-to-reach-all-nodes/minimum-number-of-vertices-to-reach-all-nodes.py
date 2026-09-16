class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        # Track which nodes have incoming edges
        has_incoming = [False] * n
        
        for u, v in edges:
            has_incoming[v] = True
            
        # Collect all nodes with zero incoming edges (in-degree == 0)
        return [i for i in range(n) if not has_incoming[i]]