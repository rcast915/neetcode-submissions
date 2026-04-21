# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        fakehead = ListNode(0,head) 
        curr = fakehead

        while curr:
            if n == count:
                curr.next = curr.next.next
            
            count  -= 1
            curr = curr.next
        
        return fakehead.next
        