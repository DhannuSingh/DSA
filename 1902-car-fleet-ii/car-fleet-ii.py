class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []  # Monotonic stack storing car indices

        for i in range(n - 1, -1, -1):
            p1, v1 = cars[i]

            while stack:
                j = stack[-1]
                p2, v2 = cars[j]

                # Car i cannot catch car j if car i is slower or at the same speed
                if v1 <= v2:
                    stack.pop()
                    continue

                # Calculate collision time between car i and car j
                time = (p2 - p1) / (v1 - v2)

                # If car j collides with its next target before car i collides with car j,
                # then car i will actually collide with the merged group ahead of car j,
                # so car j can be ignored.
                if ans[j] != -1.0 and time >= ans[j]:
                    stack.pop()
                else:
                    ans[i] = time
                    break

            stack.append(i)

        return ans