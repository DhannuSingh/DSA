# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find node before index 'a'
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next

        # Find node at index 'b'
        node_b = prev_a
        for _ in range(b - a + 1):
            node_b = node_b.next

        # Connect prev_a to head of list2
        prev_a.next = list2

        # Traverse to the tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Connect tail of list2 to the node after 'b'
        tail2.next = node_b.next

        return list1