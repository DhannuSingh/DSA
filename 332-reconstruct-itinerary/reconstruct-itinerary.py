class Solution:
    def findItinerary(self, tickets: list[list[int]]) -> list[str]:
        # Step 1: Build graph with sorted adjacency list
        graph = defaultdict(list)
        
        # Sort tickets lexicographically in reverse so we can efficiently pop() from the end
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        
        # Step 2: DFS to find Eulerian path (Hierholzer's Algorithm)
        def dfs(airport):
            while graph[airport]:
                # Pop the smallest lexicographical target (at the end of the sorted list)
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # Add node to itinerary when it has no more outgoing edges left
            itinerary.append(airport)
            
        dfs("JFK")
        
        # Reverse the post-order result to get the valid itinerary
        return itinerary[::-1]