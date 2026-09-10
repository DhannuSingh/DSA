"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        while curr:
            if curr.child:
                # Save the next node in the main list
                next_node = curr.next

                # Recursively/Iteratively flatten child list and get its tail
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next

                # Connect curr to child head
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

                # Connect child tail to saved next_node
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

            curr = curr.next

        return head