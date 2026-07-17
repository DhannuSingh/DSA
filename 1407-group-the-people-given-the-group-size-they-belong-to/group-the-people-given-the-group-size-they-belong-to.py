class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        buckets = defaultdict(list)

        for i, size in enumerate(groupSizes):
            buckets[size].append(i)

            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []

        return result