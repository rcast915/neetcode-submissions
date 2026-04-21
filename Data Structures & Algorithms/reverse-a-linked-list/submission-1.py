# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None

        newll = None
        curr = head

        while curr:
            nextcurr = curr.next
            curr.next = newll
            newll = curr

            curr = nextcurr
        
        return newll