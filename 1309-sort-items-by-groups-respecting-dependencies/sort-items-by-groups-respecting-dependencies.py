class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        # Step 1: Assign unique group IDs to ungrouped items (-1)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Step 2: Build item and group dependency graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n
        
        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for prev in range(n):
            for curr in beforeItems[prev]:
                # Add edge prev -> curr in item graph
                item_graph[curr].append(prev)
                item_indegree[prev] += 1
                
                # If they belong to different groups, add edge group[curr] -> group[prev]
                if group[curr] != group[prev]:
                    group_graph[group[curr]].append(group[prev])
                    group_indegree[group[prev]] += 1

        # Helper function for topological sort
        def topo_sort(nodes, graph, indegree):
            queue = deque([node for node in nodes if indegree[node] == 0])
            order = []
            
            while queue:
                curr = queue.popleft()
                order.append(curr)
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
            return order if len(order) == len(nodes) else []

        # Step 3: Topologically sort items and groups
        item_order = topo_sort(list(range(n)), item_graph, item_indegree)
        group_order = topo_sort(list(range(m)), group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        # Step 4: Group the topologically ordered items by their group ID
        ordered_groups = defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # Step 5: Assemble the final ordered list based on group_order
        result = []
        for grp in group_order:
            result.extend(ordered_groups[grp])

        return result