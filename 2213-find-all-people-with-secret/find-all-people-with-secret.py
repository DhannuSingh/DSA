class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # Track who knows the secret
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True

        # Group meetings by time
        time_map = defaultdict(list)
        for u, v, t in meetings:
            time_map[t].append((u, v))

        # Sort timestamps to process chronologically
        for t in sorted(time_map.keys()):
            # Build graph for meetings happening at current time t
            graph = defaultdict(list)
            meeting_people = set()

            for u, v in time_map[t]:
                graph[u].append(v)
                graph[v].append(u)
                meeting_people.add(u)
                meeting_people.add(v)

            # BFS starting from people in this time slot who ALREADY know the secret
            queue = [person for person in meeting_people if knows_secret[person]]
            
            # Spread the secret among connected people at timestamp t
            for person in queue:
                for neighbor in graph[person]:
                    if not knows_secret[neighbor]:
                        knows_secret[neighbor] = True
                        queue.append(neighbor)

        # Collect all people who know the secret
        return [i for i in range(n) if knows_secret[i]]