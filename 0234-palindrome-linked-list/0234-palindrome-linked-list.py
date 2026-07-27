# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    prev = None
    curr = slow
    while curr:
      next_temp = curr.next
      curr.next = prev
      prev = curr
      curr = next_temp

    first_half = head
    second_half = prev
    while second_half:
      if first_half.val != second_half.val:
        return False
      first_half = first_half.next
      second_half = second_half.next

    return True