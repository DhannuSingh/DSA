class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node: Node) -> None:
        # Add node right after head (MRU in this frequency bucket)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self) -> Node:
        # Remove and return the LRU node in this frequency bucket
        if self.size == 0:
            return None
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_dll = {}

    def _update_freq(self, node: Node) -> None:
        old_freq = node.freq
        dll = self.freq_to_dll[old_freq]
        dll.remove_node(node)

        if dll.size == 0:
            del self.freq_to_dll[old_freq]
            if self.min_freq == old_freq:
                self.min_freq += 1

        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_to_dll:
            self.freq_to_dll[new_freq] = DoublyLinkedList()
        self.freq_to_dll[new_freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                lru_dll = self.freq_to_dll[self.min_freq]
                evicted_node = lru_dll.remove_tail()
                del self.key_to_node[evicted_node.key]

            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].add_node(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)