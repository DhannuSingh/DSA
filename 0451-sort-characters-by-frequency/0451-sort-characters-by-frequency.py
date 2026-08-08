class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        
        for char, freq in counts.items():
            buckets[freq].append(char)
            
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for char in buckets[freq]:
                res.append(char * freq)
                
        return "".join(res)