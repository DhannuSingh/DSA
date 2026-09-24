class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        # Calculate the delta difference if the key already exists
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        # Update prefix nodes with the delta
        curr = self.root
        curr.score += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.score += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.score

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)