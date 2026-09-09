class TimeMap:

    def __init__(self):
        # Dictionary mapping key -> list of (timestamp, value) tuples
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        timestamps = self.map[key]
        # Binary search for the rightmost timestamp <= target timestamp
        idx = bisect.bisect_right(timestamps, timestamp, key=lambda x: x[0])

        if idx > 0:
            return timestamps[idx - 1][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)