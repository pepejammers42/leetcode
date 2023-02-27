# 2396. Strictly Palindromic Number

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        
        temp = ListNode(None)
        curr = temp
        curr2 = head
        curr2 = curr2.next
        
        while curr2:
            if curr2.val != 0:
                total += curr2.val
            else:
                curr.next = ListNode(total)
                curr = curr.next
                total = 0
            curr2 = curr2.next
        return temp.next
