# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        # at least 2 ele
        o, e = head, head.next
        track = head.next
        
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = track
        return head
