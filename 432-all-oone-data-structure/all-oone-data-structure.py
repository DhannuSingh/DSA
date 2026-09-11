class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.key_to_count = {}
        self.count_to_node = {}

        # Dummy head and tail nodes for doubly linked list
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node: Node, prev_node: Node) -> None:
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_to_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_to_count:
            curr_count = self.key_to_count[key]
            next_count = curr_count + 1
            curr_node = self.count_to_node[curr_count]

            # Find or create node for next_count
            if curr_node.next.count == next_count:
                next_node = curr_node.next
            else:
                next_node = Node(next_count)
                self.count_to_node[next_count] = next_node
                self._add_node_after(next_node, curr_node)

            next_node.keys.add(key)
            self.key_to_count[key] = next_count

            # Remove key from curr_node
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove_node(curr_node)
        else:
            # Key not present, count becomes 1
            self.key_to_count[key] = 1
            if self.head.next.count == 1:
                node_1 = self.head.next
            else:
                node_1 = Node(1)
                self.count_to_node[1] = node_1
                self._add_node_after(node_1, self.head)

            node_1.keys.add(key)

    def dec(self, key: str) -> None:
        if key not in self.key_to_count:
            return

        curr_count = self.key_to_count[key]
        curr_node = self.count_to_node[curr_count]

        if curr_count == 1:
            del self.key_to_count[key]
        else:
            prev_count = curr_count - 1
            if curr_node.prev.count == prev_count:
                prev_node = curr_node.prev
            else:
                prev_node = Node(prev_count)
                self.count_to_node[prev_count] = prev_node
                self._add_node_after(prev_node, curr_node.prev)

            prev_node.keys.add(key)
            self.key_to_count[key] = prev_count

        # Remove key from curr_node
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set in the last node
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        # Return any key from the set in the first node
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()