# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        num_set = set(nums)
        components = 0
        curr = head

        while curr:
            # Check if current node is part of a component and 
            # if it is the end of that component segment
            if curr.val in num_set and (curr.next is None or curr.next.val not in num_set):
                components += 1
            curr = curr.next

        return components